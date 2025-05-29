# PDF-Editor - Hintergrund-Entferner

Ein Python-Tool zum automatischen Entfernen von grauen Hintergründen aus PDF-Dateien.

## 📋 Funktionen

- ✅ Automatische Erkennung und Entfernung grauer Hintergründe
- ✅ Verarbeitung mehrseitiger PDF-Dokumente
- ✅ Anpassbarer Schwellenwert für Hintergrunderkennung
- ✅ Befehlszeilen-Interface
- ✅ Hohe Qualität durch 300 DPI Rendering

## 🚀 Installation

### Voraussetzungen

- Python 3.7 oder höher
- pip (Python Package Manager)

### Abhängigkeiten installieren

```bash
pip install -r requirements.txt
```

### Manuelle Installation der Abhängigkeiten

```bash
pip install PyMuPDF numpy Pillow
```

## 💻 Verwendung

### Kommandozeilen-Verwendung

```bash
python pdf_background_remover.py <eingabe-pdf>
```

**Beispiel:**
```bash
python pdf_background_remover.py "mein_dokument.pdf"
```

Die verarbeitete Datei wird automatisch als `mein_dokument_ohne_hintergrund.pdf` gespeichert.

### Programmatische Verwendung

```python
from pdf_background_remover import remove_background

# Standard-Schwellenwert (220)
remove_background("eingabe.pdf", "ausgabe.pdf")

# Angepasster Schwellenwert
remove_background("eingabe.pdf", "ausgabe.pdf", threshold=200)
```

## ⚙️ Parameter

- `input_pdf`: Pfad zur Eingabe-PDF-Datei
- `output_pdf`: Pfad zur Ausgabe-PDF-Datei
- `threshold`: Schwellenwert für Hintergrunderkennung (0-255, Standard: 220)
  - Höhere Werte = aggressivere Hintergrundentfernung
  - Niedrigere Werte = konservativere Hintergrundentfernung

## 🛠️ Wie es funktioniert

1. **PDF-Rendering**: Jede Seite wird mit 300 DPI gerendert
2. **Bildanalyse**: Pixel werden auf graue Hintergrundbereiche analysiert
3. **Hintergrundentfernung**: Graue Bereiche werden durch Weiß ersetzt
4. **PDF-Neuerstellung**: Verarbeitete Bilder werden in neue PDF eingefügt

## 📊 Unterstützte Dateiformate

- **Eingabe**: PDF-Dateien
- **Ausgabe**: PDF-Dateien (optimiert)

## 🔧 Fehlerbehebung

### Häufige Probleme

**"ModuleNotFoundError: No module named 'fitz'"**
```bash
pip install PyMuPDF
```

**"Memory Error bei großen PDFs"**
- Reduzieren Sie die DPI-Einstellung in der Matrix-Definition
- Verarbeiten Sie große Dateien seitenweise

**"Hintergrund wird nicht vollständig entfernt"**
- Experimentieren Sie mit verschiedenen Schwellenwerten
- Für dunklere Hintergründe: niedrigerer Schwellenwert (180-200)
- Für hellere Hintergründe: höherer Schwellenwert (230-250)

## 🤝 Beitragen

Beiträge sind willkommen! Bitte:

1. Forken Sie das Repository
2. Erstellen Sie einen Feature-Branch (`git checkout -b feature/AmazingFeature`)
3. Committen Sie Ihre Änderungen (`git commit -m 'Add some AmazingFeature'`)
4. Pushen Sie den Branch (`git push origin feature/AmazingFeature`)
5. Öffnen Sie eine Pull Request

## 📝 Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Siehe `LICENSE`-Datei für Details.

## 👨‍💻 Autor

Erstellt mit ❤️ für eine bessere PDF-Bearbeitung

## 🙏 Danksagungen

- [PyMuPDF](https://pymupdf.readthedocs.io/) für PDF-Verarbeitung
- [NumPy](https://numpy.org/) für effiziente Array-Operationen
- [Pillow](https://pillow.readthedocs.io/) für Bildverarbeitung 