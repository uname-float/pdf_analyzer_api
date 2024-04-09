from fastapi import FastAPI, UploadFile, File
#from pdf_analyzer import PDFAnalyzer

app = FastAPI()
#pdf_analyzer = PDFAnalyzer()

@app.get("/")
def index():
    return {"Hello": "World"}

@app.post("/analyze-pdf/")
async def analyze_pdf(file: UploadFile = File(...)):
    # Salva il file PDF su disco
    with open("temp.pdf", "wb") as pdf_file:
        pdf_file.write(await file.read())

    # Analizza il file PDF
    results = pdf_analyzer.analyze_pdf("temp.pdf")

    # Rimuovi il file temporaneo
    os.remove("temp.pdf")

    return results

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

