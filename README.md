# Cartoonizer App

Trasforma le tue foto in veri e propri cartoni animati.
Questa applicazione utilizza OpenCV e tecniche di elaborazione delle immagini per creare effetti **cartoon**, regolare **saturazione**, **luminosità**, e applicare filtri artistici personalizzati.  

---

## Caratteristiche principali

- **Cartoonizzazione automatica** delle immagini
- **Filtri regolabili**:
  - Sfocatura (`blur`)
  - Edge cut
  - Saturazione
  - Luminosità
  - Effetto “paint”
  - Numero di colori per posterizzazione
- **Anteprima in tempo reale**
- **Salvataggio rapido** delle immagini elaborate

---

## 🚀 Tecnologie utilizzate

- Python 3.12
- [OpenCV](https://opencv.org/) – elaborazione immagini
- [scikit-learn](https://scikit-learn.org/) – KMeans per posterizzazione colori
- [Gradio](https://gradio.app/) – interfaccia web interattiva
- [NumPy](https://numpy.org/) – gestione array

---

## ⚡ Come usare

1. Clona il repository:
    ```bash
    git clone https://github.com/tuo-username/cartoonizer.git
    cd cartoonizer
    ```

2. Crea un ambiente virtuale e installa le dipendenze:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # su Windows: .venv\Scripts\activate
    pip install -r requirements.txt
    ```

3. Avvia l’app:
    ```bash
    python app.py
    ```

4. Apri il browser all’indirizzo mostrato da Gradio, carica la tua immagine e inizia a modificare i parametri.

---

## Parametri personalizzabili

| Parametro        | Descrizione                                  | Valori consigliati |
|-----------------|---------------------------------------------|-----------------|
| **Sfocatura**    | Intensità della sfocatura del bordo         | 0 – 10          |
| **Edge Cut**     | Sensibilità del rilevamento dei bordi       | 0 – 9           |
| **Saturazione**  | Intensità dei colori                        | 0 – 50          |
| **Luminosità**   | Aumenta o diminuisce la luminosità          | 0 – 50          |
| **Modalità Paint** | Intensità dell’effetto pittorico          | 0 – 9           |
| **Numero colori** | Quantità di colori nella posterizzazione   | 2 – 20          |

---

## 💾 Salvataggio immagini

- Una volta applicati i filtri, puoi **salvare l’immagine cartoonizzata** direttamente tramite l’interfaccia.
- Le immagini vengono salvate in una cartella temporanea con un suffisso `_cartoonized`.

---

## Screenshot

*(Inserisci qui le immagini prima/dopo del cartoonizer)*

| Immagine orgiginale        | Cartoonize!|
|-------------------------------------------------------|-------------------------------------------------------|
|![Cane_dalmata](https://github.com/user-attachments/assets/2a272318-20ed-405a-8428-3b672d8ed617)|<img width="960" height="1280" alt="cartoonized_image(2)" src="https://github.com/user-attachments/assets/ba036a9b-0476-459f-bed5-fd510df5e976" />|


---

## 📝 Note

- Alcune immagini con colori particolari potrebbero richiedere **piccole regolazioni dei parametri** per ottenere il miglior risultato.
- L’applicazione mantiene la conversione tra **RGB e BGR** corretta per evitare problemi di colori invertiti.

---
