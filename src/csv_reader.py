import csv

def read_csv_lines(path):
    """
    Lee un archivo CSV y devuelve todas las filas como texto plano.
    """

    lines = []

    with open(path, newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            lines.append(" ".join(row))

    return lines
