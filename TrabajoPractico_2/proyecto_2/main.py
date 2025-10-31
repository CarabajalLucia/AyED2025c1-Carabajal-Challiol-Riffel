from modules2.temperaturas_avl import Temperaturas_DB

if __name__ == "__main__":
    db = Temperaturas_DB()

    # Cargar el txt
    db.cargar_archivo("muestras.txt")
    print("Cantidad de muestras cargadas:", db.cantidad_muestras())

    """ejemplos
    print("\nTemperatura el 02/01/2025:", db.devolver_temperatura("02/01/2025"))
    print("Máxima entre 02/01/2025 y 22/01/2025:", db.max_temp_rango("02/01/2025", "22/01/2025"))
    print("Mínima entre 02/01/2025 y 22/01/2025:", db.min_temp_rango("02/01/2025", "22/01/2025"))

    print("\nListado entre 02/01/2025 y 22/01/2025:")
    for t in db.devolver_temperaturas("02/01/2025", "22/01/2025"):
        print(" ", t)
"""
    # Muestra la grafica del arbol
    db.graficar_arbol()
