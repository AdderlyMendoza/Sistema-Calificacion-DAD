respuestas_P = "AAADEEDCBA"
respuestas_Q = "BBBBAABBAE"
respuestas_R = "CCDCBBDAAA"
respuestas_S = "ADCDEEDDEA"
respuestas_T = "CDEDEEDBDA"

comparacion_rpta = ""
rptaFijas = ""

# Abre el archivo en modo lectura
with open('data-cal.txt', 'r') as archivo:
    for linea in archivo:
        datosSeparados = linea.split() # .split(",")
        
        # Asignamos cada parte a una variable
        dni = datosSeparados[0]
        tipo_prueba = datosSeparados[1]   
        salon = datosSeparados[2]          
        rpta_postulante = datosSeparados[3]     
        
        print(dni,tipo_prueba,rpta_postulante)
        
        comparacion_rpta = ""
        
        if( tipo_prueba == "P"):
            rptaFijas = respuestas_P
        if( tipo_prueba == "Q"):
            rptaFijas = respuestas_Q
        if( tipo_prueba == "R"):
            rptaFijas = respuestas_R
        if( tipo_prueba == "S"):
            rptaFijas = respuestas_S
        if( tipo_prueba == "T"):
            rptaFijas = respuestas_T
        
        for letra1, letra2 in zip(rpta_postulante, rptaFijas):
            if letra1 == letra2:
                comparacion_rpta += letra1  # Añadir la letra igual a la cadena de resultados
            else:
                comparacion_rpta += "-"  # Si no son iguales, puedes agregar un marcador de diferencia
        print(comparacion_rpta)
