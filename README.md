# PDF Analyzer API

Questo progetto implementa un'API FastAPI per l'analisi delle bollette in formato PDF, consentendo agli utenti di estrarre informazioni e dati pertinenti dalle loro bollette.

## Descrizione

L'API fornisce una serie di endpoint per eseguire operazioni di analisi sui file PDF delle bollette. Gli utenti possono inviare file PDF tramite l'API e ricevere in risposta informazioni estratte come costi, consumi, dettagli contrattuali, ecc.

## Struttura del progetto

Il progetto è organizzato come segue:

- `app`: Cartella principale dell'applicazione.
  - `analyzer.py`: Contiene le funzionalità per l'analisi dei PDF.
  - `api.py`: Definisce le rotte e le operazioni dell'API FastAPI.
  - `main.py`: File principale dell'applicazione FastAPI.
- `requirements.txt`: Elenco delle dipendenze del progetto.
- `README.md`: Documentazione del progetto.

## Installazione

Per eseguire il progetto in locale, segui questi passaggi:

1. Clona il repository:


2. Installa le dipendenze:


3. Avvia l'applicazione:


L'applicazione sarà ora disponibile all'indirizzo `http://localhost:8000`.

## Utilizzo

Una volta avviata l'applicazione, puoi accedere alla documentazione API interattiva tramite il browser all'indirizzo `http://localhost:8000/docs`. Da qui, puoi esplorare gli endpoint disponibili e inviare richieste per analizzare i tuoi file PDF.

## Contributi

Sono benvenuti i contributi a questo progetto! Se desideri contribuire, apri una nuova issue o invia una pull request.

## Licenza

Questo progetto è distribuito con la licenza MIT. Per ulteriori informazioni, consulta il file LICENSE.

