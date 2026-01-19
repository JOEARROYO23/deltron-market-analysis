import re

def parse_lines(lines):
    """
    Analiza líneas de texto y extrae productos con precios en soles.

    :param lines: Lista de líneas de texto (PDF o CSV)
    :return: Lista de diccionarios con descripción y precio
    """

    products = []

    for line in lines:
        line = line.strip()

        # Ignorar líneas muy cortas o irrelevantes
        if len(line) < 10:
            continue

        # Buscar precios en soles (ej: S/ 599.00)
        price_match = re.search(r"S/\s*(\d+(?:\.\d{2})?)", line)

        if price_match:
            try:
                precio = float(price_match.group(1))

                # Limpiar la descripción quitando el precio
                descripcion = re.sub(r"S/\s*\d+(?:\.\d{2})?", "", line)
                descripcion = descripcion.replace("  ", " ").strip()

                products.append({
                    "descripcion": descripcion,
                    "precio": precio
                })

            except ValueError:
                # Si el precio no se puede convertir, se ignora
                continue

    return products


