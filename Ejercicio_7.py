def agregar_item(inventario, item):
   ### Añade un ítem al inventario si no existe ya.
    if item in inventario:
        raise ValueError(f"El ítem '{item}' ya está en el inventario.")
    inventario.append(item)

def main():
    """Función principal del programa."""
    # Inventario inicial
    inventario = ["espada", "escudo", "poción"]
    
    # Ítems a añadir
    nuevos_items = ["arco", "flecha", "poción"]
    
    for item in nuevos_items:
        try:
            agregar_item(inventario, item)
            print(f"Ítem '{item}' añadido al inventario.")
        except ValueError as e:
            print(e)
    
    # Mostrar inventario final
    print("Inventario final:", inventario)

# Ejecutar el programa
if __name__ == "__main__":
    main()