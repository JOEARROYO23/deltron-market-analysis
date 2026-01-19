 from pdf_reader import read_pdf_lines
from exporter import export_to_csv
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

    # Leer datos (PDF o CSV)
    lines = load_data(file_path)

    # Procesar líneas para obtener productos
    products = parse_lines(lines)

    print(f"Líneas procesadas: {len(lines)}")
    print(f"Productos detectados: {len(products)}")

    # Exportar resultados a CSV
    output_path = "data/processed/deltron_productos.csv"
    export_to_csv(products, output_path)

    print("Exportación completada:", output_path)

