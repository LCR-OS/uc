# uc

# Universal Converter

Nome progetto: Universal Converter (UC)

Tecnologie usate: Python, Pillow, Tkinter

Descrizione:
Universal Converter è un convertitore di file offline e open source. È nato come alternativa ai siti di conversione online ricchi di pubblicità invasive e con possibili problemi di privacy. Attualmente utilizza Pillow come primo motore di conversione per le immagini, ma l'obiettivo è evolverlo in un'applicazione modulare capace di scegliere automaticamente il motore migliore (Pillow, FFmpeg, LibreOffice, ecc.) in base al tipo di conversione richiesta.

File inviati:
- UniversalConverter.zip
- README.md

Perché includo archivi/binari:
L'archivio contiene il codice sorgente del progetto e la struttura completa della repository.

Istruzioni di esecuzione / note di sicurezza:
Richiede Python 3 e la libreria Pillow (`pip install pillow`). Avviare il file principale del progetto. Il software esegue esclusivamente conversioni locali: nessun file viene inviato a server esterni o servizi online.

Problemi o richieste di feedback:
Mi interessa ricevere feedback sull'architettura del progetto, sulla qualità del codice Python, sull'organizzazione della repository e su possibili miglioramenti per rendere il progetto facilmente estendibile con nuovi motori di conversione.

Screenshot / immagini:
(al momento nessuno)

Cosa ho già provato:
- Separazione tra GUI, motore di conversione e gestione degli errori.
- Prima organizzazione del codice in funzioni dedicate.
- Gestione delle eccezioni più comuni.
- Pianificazione di un'architettura basata su motori di conversione indipendenti.

## EN

**Free, offline and open-source file converter.**

Convert your files locally without uploading them to websites full of ads, trackers or privacy concerns.

## Features

- Offline conversion
- Open Source
- Cross-platform
- Built in Python
- Currently powered by Pillow
- Easily extensible with new conversion engines

## Why?

Many free conversion websites:

- upload your files to remote servers;
- show misleading advertisements;
- have file size limits;
- require subscriptions.

Universal Converter performs conversions locally on your computer.

**Your files never leave your machine.**

## Roadmap

- Multiple conversion engines
- Drag & Drop
- Batch conversion
- Command-line interface (CLI)
- Plugin system



## IT

**Convertitore di file gratuito, offline e open source.**

Converti i tuoi file direttamente sul tuo computer, senza caricarli su siti web pieni di pubblicità invasive, tracker o problemi di privacy.

## Caratteristiche

- Conversione completamente offline
- Open Source
- Multipiattaforma
- Sviluppato in Python
- Attualmente utilizza Pillow come motore di conversione
- Facilmente estendibile con nuovi motori di conversione

## Perché?

Molti siti gratuiti per la conversione dei file:

- caricano i tuoi file su server remoti;
- mostrano pubblicità ingannevoli o invasive;
- impongono limiti sulla dimensione dei file;
- richiedono abbonamenti per sbloccare tutte le funzionalità.

Universal Converter esegue tutte le conversioni direttamente sul tuo computer.

**I tuoi file non lasciano mai il tuo dispositivo.**

## Roadmap

- Supporto a più motori di conversione
- Drag & Drop
- Conversione multipla (Batch)
- Interfaccia da riga di comando (CLI)
- Sistema di plugin