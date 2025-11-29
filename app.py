import cv2
import os
import numpy as np
import gradio as gr
from sklearn.cluster import KMeans
import uvicorn
import tempfile


# -----------------------------
#   FUNZIONI
# -----------------------------

def posterize (image, colors: int):
  data = image.reshape(-1, 3).astype(np.float32)

  kmeans = KMeans(n_clusters=colors, random_state=42, n_init='auto')
  kmeans.fit(data)

  labels = kmeans.predict(data)

  centers = np.uint8(kmeans.cluster_centers_)
  posterized_image = centers[labels]
  posterized_image = posterized_image.reshape(image.shape)

  return posterized_image

def adjust_image (image, saturation: int, brightness: int):
  hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
  h, s, v = cv2.split(hsv_image)

  s = cv2.add(s, saturation)  # Increase saturation by adding a constant
  s = np.clip(s, 0, 255) # Clip values to 0-255

  v = cv2.add(v, brightness)  # Increase brightness by adding a constant
  v = np.clip(v, 0, 255) # Clip values to 0-255

  adjusted_hsv = cv2.merge([h, s, v])
  adjusted_color_image = cv2.cvtColor(adjusted_hsv, cv2.COLOR_HSV2BGR)
  return adjusted_color_image


def cartoonize (image, saturation: int, brightness: int, edge_cut: int, paint_effect: int, blur: int , colors: int):
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  gray = cv2.medianBlur(gray, blur)
  adjusted_color_image = adjust_image(image, saturation, brightness)
  posterized_image = posterize(adjusted_color_image, colors)
  edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, edge_cut)
  color = cv2.bilateralFilter(posterized_image, paint_effect*2+1, 250, 250)
  cartoon = cv2.bitwise_and(color, color, mask=edges)
  return cartoon

# -----------------------------
#   FILTRI
# -----------------------------

def apply_filters(image, blur, edge_cut, saturation, brightness, paint_effect, colors):

    if image is None:
        return None
    
    # Convertiamo da RGB (Gradio) a BGR (OpenCV)
    img = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
   
    cartoonized = cartoonize(img,saturation,brightness,edge_cut,paint_effect,blur,colors)

    cartoonized = cv2.cvtColor(cartoonized, cv2.COLOR_BGR2RGB)

    return cartoonized

  
with gr.Blocks() as demo:
    gr.Markdown("# Cartoonizer")

    with gr.Row():
        input_img = gr.Image(label="Carica immagine",type='numpy')
        output_img = gr.Image(label="Risultato")

    with gr.Accordion("Filtri", open=True):
        blur = gr.Slider(0, 10, value=5, step=1, label="Sfocatura")
        edge_cut = gr.Slider(0, 9, value=4, step=1, label="Edge Cut")
        saturation = gr.Slider(0, 50, value=30, step=5, label="Saturazione")
        brightness = gr.Slider(0, 50, value=15, step=5, label="Luminosità")
        paint_effect = gr.Slider(0, 9, value=9, step=1, label="Modalità Paint")
        colors = gr.Slider(0, 20, value=12, step=1, label="Numero di colori")

    btn = gr.Button("Applica Filtri")
    save = gr.Button("Salva Immagine")

    # Aggiornamento in tempo reale
    btn.click(
        apply_filters,
        inputs=[input_img, blur, edge_cut, saturation,brightness,paint_effect, colors],
        outputs=output_img
    )

    # Salvataggio file
    
    def save_image(image):
        if image is None:
            return None
        
        tmp_path = os.path.join(
            tempfile.gettempdir(),
            "cartoonized_image.png"  # fixed name or generate unique
        )
        bgr = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        cv2.imwrite(tmp_path, bgr)
        return tmp_path

    save.click(save_image, inputs=output_img, outputs=gr.File(label="File Salvato"))

# Avvio app
demo.launch(debug=True)