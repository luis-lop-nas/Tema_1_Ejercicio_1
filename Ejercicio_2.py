# Programa para calcular el interés compuesto

def leer_tasa_interes():
    """Lee la tasa de interés anual (entre 1% y 10%) del usuario."""
    while True:
        try:
            tasa_interes = float(input("Introduce la tasa de interés anual (entre 1 y 10): "))
            if 1 <= tasa_interes <= 10:
                return tasa_interes / 100  # Convertir a decimal
            else:
                print("Por favor, introduce un valor entre 1 y 10.")
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número.")

def leer_anios():
    """Lee el número de años (positivo) del usuario."""
    while True:
        try:
            anios = int(input("Introduce el número de años: "))
            if anios > 0:
                return anios
            else:
                print("Por favor, introduce un número positivo.")
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número entero.")

def calcular_interes_compuesto(capital_inicial, tasa_interes, anios):
    """Calcula el capital final usando la fórmula del interés compuesto."""
    return capital_inicial * (1 + tasa_interes) ** anios

def main():
    """Función principal del programa."""
    print("Su capital inicial es de $1000.")
    capital_inicial = 1000
    tasa_interes = leer_tasa_interes()
    anios = leer_anios()
    capital_final = calcular_interes_compuesto(capital_inicial, tasa_interes, anios)
    print(f"El capital final después de {anios} años es: {capital_final:.2f}")

# Ejecutar el programa
if __name__ == "__main__":
    main()