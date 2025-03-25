from collections import deque

def crear_cola_misiones(misiones):
    """
    Crea una cola con las misiones ordenadas por dificultad.
    Los números de dificultad no se muestran en la cola.
    """
    # Ordenar las misiones por dificultad (segundo elemento de cada tupla)
    misiones_ordenadas = sorted(misiones, key=lambda m: m[1])
    
    # Crear una cola con solo los nombres de las misiones
    cola_misiones = deque([m[0] for m in misiones_ordenadas])
    return cola_misiones

def mostrar_misiones(cola_misiones):
    """Muestra las misiones en la cola."""
    print("Misiones en orden de dificultad:")
    for mision in cola_misiones:
        print(f"- {mision}")

def main():
    """Función principal del programa."""
    # Lista de misiones con sus niveles de dificultad
    misiones = [
        ("Rescatar al aldeano", 3),
        ("Derrotar al dragón", 10),
        ("Recolectar hierbas", 1),
        ("Explorar la cueva", 5),
        ("Defender la aldea", 7)
    ]
    
    # Crear la cola de misiones
    cola_misiones = crear_cola_misiones(misiones)
    
    # Mostrar las misiones en orden de dificultad
    mostrar_misiones(cola_misiones)

# Ejecutar el programa
if __name__ == "__main__":
    main()