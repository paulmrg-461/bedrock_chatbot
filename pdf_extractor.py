import PyPDF2

class PdfExtractor:
    def __init__(self, pdf_path):
        """
        Inicializa la clase con la ruta del archivo PDF.
        
        :param pdf_path: Ruta al archivo PDF.
        """
        self.pdf_path = pdf_path
    
    def extract_text(self):
        """
        Extrae y retorna el texto del archivo PDF completo.
        
        :return: Texto extraído del PDF.
        """
        try:
            with open(self.pdf_path, 'rb') as file:
                reader = PyPDF2.PdfFileReader(file)
                text = ''
                for page_num in range(reader.numPages):
                    text += reader.getPage(page_num).extract_text()
            return text
        except Exception as e:
            print(f"Error al extraer el texto: {str(e)}")
            return None