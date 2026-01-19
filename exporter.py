import csv

def export_to_csv(products, output_path):
    """
    Exporta una lista de productos a un archivo CSV.
    """

    with open(output_path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        # Encabezados
        writer.writerow(["descripcion", "precio"])

        # Datos
        for product in products:
            writer.writerow([
                product["descripcion"],
                product["precio"]
            ])
