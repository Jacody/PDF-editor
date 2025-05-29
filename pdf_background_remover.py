#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import fitz  # PyMuPDF
import numpy as np
from PIL import Image
import io
import os
import sys

def remove_background(input_pdf, output_pdf, threshold=220):
    """
    Entfernt den grauen Hintergrund aus einer PDF-Datei.
    
    Args:
        input_pdf (str): Pfad zur Eingabe-PDF-Datei
        output_pdf (str): Pfad zur Ausgabe-PDF-Datei
        threshold (int): Schwellenwert für die Erkennung des Hintergrunds (0-255)
    """
    print(f"Verarbeite PDF: {input_pdf}")
    
    # Öffne die PDF-Datei
    pdf_document = fitz.open(input_pdf)
    output_document = fitz.open()
    
    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]
        
        # Rendere die PDF-Seite als Pixmap mit hoher Auflösung
        pix = page.get_pixmap(matrix=fitz.Matrix(300/72, 300/72))
        
        # Konvertiere zu einem PIL-Bild
        img_data = pix.samples
        img = Image.frombytes("RGB", [pix.width, pix.height], img_data)
        
        # Konvertiere zu NumPy-Array für die Bildverarbeitung
        img_array = np.array(img)
        
        # Erstelle eine Maske für die Hintergrundbereiche
        # Wir nehmen an, dass der Hintergrund grau ist
        is_light_gray = np.all(img_array > threshold, axis=2) | (
            (img_array[:,:,0] > threshold-30) & 
            (img_array[:,:,1] > threshold-30) & 
            (img_array[:,:,2] > threshold-30)
        )
        
        # Setze alle Hintergrundpixel auf Weiß
        white_rgb = np.array([255, 255, 255], dtype=np.uint8)
        img_array[is_light_gray] = white_rgb
        
        # Konvertiere zurück zu einem PIL-Bild
        processed_img = Image.fromarray(img_array)
        
        # Speichere das Bild in einem Byte-Stream
        img_byte_arr = io.BytesIO()
        processed_img.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)
        
        # Erstelle eine neue PDF-Seite
        new_page = output_document.new_page(width=page.rect.width, height=page.rect.height)
        
        # Füge das verarbeitete Bild zur neuen Seite hinzu
        new_page.insert_image(rect=page.rect, stream=img_byte_arr.getvalue())
        
        print(f"Seite {page_num + 1}/{pdf_document.page_count} verarbeitet")
    
    # Speichere die neue PDF
    output_document.save(output_pdf)
    output_document.close()
    pdf_document.close()
    
    print(f"Fertig! PDF ohne Hintergrund gespeichert unter: {output_pdf}")

def main():
    if len(sys.argv) > 1:
        input_pdf = sys.argv[1]
        
        # Erzeuge Ausgabedateinamen
        filename, ext = os.path.splitext(input_pdf)
        output_pdf = f"{filename}_ohne_hintergrund{ext}"
        
        # Entferne Hintergrund
        remove_background(input_pdf, output_pdf)
    else:
        # Verwende den in der Anfrage angegebenen Pfad
        input_pdf = '/Users/Coby/Desktop/GitHub/beamer-games/Master Zeugnis.pdf'
        output_pdf = '/Users/Coby/Desktop/GitHub/beamer-games/Master Zeugnis_ohne_hintergrund.pdf'
        remove_background(input_pdf, output_pdf)

if __name__ == "__main__":
    main() 