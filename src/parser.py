import re

def parse_lines(lines):
    """
    Recibe líneas de texto extraídas del PDF
    y devuelve una lista de productos con precios.
    """

    products = []

    for line in lines:
        # Buscar precios en soles (S/ 123.45)
        match = re.search(r"S/\s*\d+(\.\d{2})?", line)

        if match:
            products.append({
                "raw_line": line.strip(),
                "precio": match.group()
            })

    return products

