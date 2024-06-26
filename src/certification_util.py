import PyPDF2

class CertificationUtil:

    # Function to extract text from PDF. Assuming that we are loading only one pdf page
    @staticmethod
    def extract_text_from_pdf(file_path):
        text = ""
        with open(file_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            if len(reader.pages) > 0:
                page = reader.pages[0]
                text = page.extract_text()
        return text