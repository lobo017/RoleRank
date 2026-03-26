import docx

class DocxExtractor:
    def __init__(self, path):
        self.path = path

    def extract_text(self):
        with open(self.path, "rb") as file:
            doc = docx.Document(file)
            text = ""
            for paragraph in doc.paragraphs:
                text += paragraph.text + "\n"
        return text