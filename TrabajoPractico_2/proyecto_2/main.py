# PROGRAMA PRINCIPAL 
from modules2.temperaturas_avl import Temperaturas_DB
if __name__ == "__main__":
    # Creamos una instancia de la base de datos
    db = Temperaturas_DB()

    # Abrimos el archivo de muestras
    with open("muestras.txt", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if not linea:
                continue
            # Separar fecha y temperatura usando ';' como separador
            fecha_str, temp_str = linea.split(";")
            temperatura = float(temp_str)
            db.guardar_temperatura(temperatura, fecha_str)

    # Mostramos la cantidad total de muestras cargadas
    print("Cantidad de muestras cargadas:", db._cantidad)
