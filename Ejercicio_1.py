def formatear_receta(cadena_corrupta):
    # Voltear la cadena
    cadena_volteada = cadena_corrupta[::-1]

    # Separar el nombre de la receta y las calorías
    partes = cadena_volteada.split(" ", 2)  # Dividir en solo dos partes
    calorias = partes[1]  # Obtener el número de calorías
    nombre_receta = partes[2]  # El resto es el nombre de la receta

    # Formatear el texto
    return f"La receta de {nombre_receta} contiene {calorias} calorías."

# Ejemplo de uso
cadena_corrupta = "sáirotaloc 052 al ed atceR"  # Ejemplo de cadena corrupta
print(formatear_receta(cadena_corrupta))