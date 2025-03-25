import sys

def descomponer_ip(direccion_ip):
    """
    Descompone una dirección IP en sus cuatro octetos y los muestra línea a línea.
    """
    octetos = direccion_ip.split(".")
    if len(octetos) != 4 or not all(o.isdigit() and 0 <= int(o) <= 255 for o in octetos):
        print("Error: La dirección IP no es válida.")
        return

    print("Octetos de la dirección IP:")
    for i, octeto in enumerate(octetos, start=1):
        print(f"Octeto {i}: {octeto}")


def main():
    """Función principal del script."""
    if len(sys.argv) != 2:
        print("Uso: python Ejercicio_5.py <dirección_ip>")
        return

    direccion_ip = sys.argv[1]
    descomponer_ip(direccion_ip)

# Ejecutar el script
if __name__ == "__main__":
    main()
