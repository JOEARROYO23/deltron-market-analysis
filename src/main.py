from pdf_reader import read_pdf_lines
from csv_reader import read_csv_lines
from parser import parse_lines
import os

def load_data(file_path):
    """
    Carga datos desde un archivo PDF o CSV según su extensión.
    """

    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".pdf":
        return read_pdf_lines(file_path)
    elif extension == ".csv":
        return read_csv_lines(file_path)
    else:
        raise ValueError("Formato de archivo no soportado")

if __name__ == "__main__":
    file_path = "data/raw/input_file"

    lines = load_data(file_path)
    products = parse_lines(lines)

    print(f"Líneas procesadas: {len(lines)}")
    print(f"Productos detectados: {len(products)}")
