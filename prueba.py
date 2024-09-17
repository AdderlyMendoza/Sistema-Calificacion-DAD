import shlex

# Abre el archivo en modo lectura
with open('data-cal.txt', 'r') as archivo:
    for linea in archivo:
        # Usamos shlex.split() para dividir la línea respetando las comillas
        partes = shlex.split(linea)
        
        # Asignamos cada parte a una variable
        dni = partes[0]           # '12345678'
        tip_pr = partes[1]        # 'P'
        salon = partes[2]         # '189'
        respuestas = partes[3]    # 'A ADECBADE' (sin las comillas)

        # Imprimimos los resultados
        print(f"DNI: {dni}")
        print(f"Tipo de prueba: {tip_pr}")
        print(f"Salón: {salon}")
        print(f"Respuestas: {respuestas}")
        print("---------------------------------------")
