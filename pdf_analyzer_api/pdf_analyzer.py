import re
import sys
import pdfplumber

from tqdm import tqdm

class PDFAnalyzer:
    # Metodi della classe...
    def __init__(self, pdf_file):
        self.pdf_file = pdf_file

    def ricerca_keyword(self, keywords):
        risultati = []
        seriale = []

        with pdfplumber.open(self.pdf_file) as pdf:
            num_pages = len(pdf.pages)
            for page_number in tqdm(range(num_pages), desc="Processing pages", unit="page"):
                page = pdf.pages[page_number]
                text = page.extract_text()

                # Stampa l'avanzamento
                print(f"Sto analizzando la pagina {page_number + 1}/{num_pages}...")

                # Utilizza espressioni regolari per trovare numeri adiacenti alle parole chiave "costo" o "pagare"
                matches = re.findall(r"(?:costo|pagare)\s*:\s*(\d+(?:\.\d+)?)", text, re.IGNORECASE)

                for match in matches:
                    seriale.append({
                        "parola_chiave": "costo/pagare",
                        "valore": match,
                        "pagina": page.page_number + 1,
                        "testo": text
                })

                for keyword in keywords:
                    if keyword in text:
                        risultati.append({
                            "parola_chiave": keyword,
                            "pagina": page.page_number + 1,
                            "testo": text
                        })

        return risultati

    def scrivi_risultati(self, risultati, output_file):
        with open(output_file, "w") as file:
            for risultato in risultati:
                file.write(f"Parola chiave: {risultato['parola_chiave']}\n")
                file.write(f"Pagina: {risultato['pagina']}\n")
                file.write(f"Testo:\n{risultato['testo']}\n\n")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Utilizzo: python script.py <file_pdf> <parole_chiave>")
        sys.exit(1)

    pdf_file = sys.argv[1]
    parole_chiave = sys.argv[2:]

    pdf_analyzer = PDFAnalyzer(pdf_file)
    risultati_ricerca = pdf_analyzer.ricerca_keyword(parole_chiave)
    pdf_analyzer.scrivi_risultati(risultati_ricerca, "risultati.txt")

