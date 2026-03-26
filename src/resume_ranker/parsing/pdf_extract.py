import pdfplumber

class PDFExtractor:
    def __init__(self, path):
        self.path = path

    def extract_text(self):
        with pdfplumber.open(self.path) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text()
        return text