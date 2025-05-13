from pdfminer.high_level import extract_text
import docx

def extract_raw_data(filepath):
    if filepath.endswith('.pdf'):
        try:
            return extract_text(filepath)
        except Exception as e:
            return f"Error extrayendo texto del PDF: {e}"
    elif filepath.endswith('.docx'):
        try:
            doc = docx.Document(filepath)
            return '\n'.join([p.text for p in doc.paragraphs])
        except Exception as e:
            return f"Error extrayendo texto del DOCX: {e}"
    else:
        return "Formato de archivo no soportado"