
import fitz  # PyMuPDF
import os

def extract_text_from_pdf(pdf_path, save_to):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()

    filename = os.path.splitext(os.path.basename(pdf_path))[0] + ".txt"
    full_path = os.path.join(save_to, filename)

    with open(full_path, "w", encoding="utf-8") as f:
        f.write(text)

    return full_path
