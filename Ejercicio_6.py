def clasificar_personajes(personajes):
    
    humanos = sorted([nombre for nombre, tipo in personajes if tipo == "humano"])
    no_humanos = sorted([nombre for nombre, tipo in personajes if tipo == "no humano"])
    return humanos, no_humanos

def main():
    
    # Lista de personajes (nombre, tipo)
    personajes = [
        ("Mario", "humano"),
        ("Bowser", "no humano"),
        ("Link", "humano"),
        ("Kirby", "no humano"),
        ("Samus", "humano"),
        ("Pikachu", "no humano")
    ]
    
    # Clasificar personajes
    humanos, no_humanos = clasificar_personajes(personajes)
    
    # Mostrar resultados
    print("Personajes humanos:", humanos)
    print("Personajes no humanos:", no_humanos)

# Ejecutar el programa
if __name__ == "__main__":
    main()