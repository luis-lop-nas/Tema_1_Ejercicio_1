def palabras_comunes(lista1, lista2):
    """Genera una lista con las palabras comunes entre dos listas, sin repeticiones."""
    # Convertir las listas a conjuntos para eliminar duplicados y encontrar intersección
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)
    return list(conjunto1 & conjunto2)  # Intersección de conjuntos convertida a lista

def main():
    """Función principal del programa."""
    # Ejemplo de listas
    lista1 = ["manzana", "pera", "uva", "manzana", "naranja"]
    lista2 = ["pera", "naranja", "kiwi", "uva", "uva"]

    # Obtener palabras comunes
    resultado = palabras_comunes(lista1, lista2)

    # Mostrar el resultado
    print("Palabras comunes entre ambas listas:", resultado)

# Ejecutar el programa
if __name__ == "__main__":
    main()