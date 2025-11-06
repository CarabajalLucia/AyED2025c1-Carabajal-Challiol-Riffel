from modules2.temperaturas_avl import Temperaturas_DB

if __name__ == "__main__":
    datos = Temperaturas_DB()

    # cargar los datos
    datos.cargar_archivo("muestras.txt")
    print("Cantidad de muestras cargadas:", datos.cantidad_muestras())

"""ejemplos
    print("\nTemperatura el 02/01/2025:", datos.devolver_temperatura("02/01/2025"))
    print("Máxima entre 02/01/2025 y 22/01/2025:", datos.max_temp_rango("02/01/2025", "22/01/2025"))
    print("Mínima entre 02/01/2025 y 22/01/2025:", datos.min_temp_rango("02/01/2025", "22/01/2025"))

    print("\nListado entre 02/01/2025 y 22/01/2025:")
    for t in datos.devolver_temperaturas("02/01/2025", "22/01/2025"):
        print(" ", t)"""

    # muetra grafica del aarbol
datos.graficar_arbol()
