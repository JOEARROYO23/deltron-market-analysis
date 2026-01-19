import pdfplumber

# --------------------------------------------------
# Lee un archivo PDF y extrae todas las líneas de texto
# Este módulo se usa para procesar listas de precios de Deltron
# --------------------------------------------------
def read_pdf_lines(path):
    """
    Lee un archivo PDF y devuelve todas las líneas de texto encontradas.

    :param path: Ruta del archivo PDF
    :return: Lista de líneas de texto extraídas del PDF
    """

    lines = []

    # Abrir el archivo PDF usando pdfplumber
    with pdfplumber.open(path) as pdf:
        # Recorrer cada página del PDF
        for page in pdf.pages:
            text = page.extract_text()

            # Si la página contiene texto, separarlo por líneas
            if text:
                page_lines = text.split("\n")
                lines.extend(page_lines)

    return lines






