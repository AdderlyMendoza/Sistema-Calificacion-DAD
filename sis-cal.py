import shlex

respuestas_P = "AAADEEDCBA"
respuestas_Q = "BBBBAABBAE"
respuestas_R = "CCDCBBDAAA"
respuestas_S = "ADCDEEDDEA"
respuestas_T = "CDEDEEDBDA"

comparacion_rpta = ""
rptaFijas = ""
puntaje = 0

# Abre el archivo en modo lectura
with open('data-cal.txt', 'r') as archivo:
    for linea in archivo:
        # datosSeparados = linea.split() # .split(",")
        datosSeparados = shlex.split(linea) # shlex.split() para dividir la línea respetando las comillas
        
        # Asignamos cada parte a una variable
        dni, tipo_prueba, salon, rpta_postulante = datosSeparados   
        
        print(dni,tipo_prueba,rpta_postulante)
        
        comparacion_rpta = ""
        puntaje = 0
        
        
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
                comparacion_rpta += letra1  # si es igual las RPTAS
                puntaje = puntaje + 20
            else:
                comparacion_rpta += "-" 
        #print(comparacion_rpta, puntaje)
        
        puntaje = 1
        
        Ponderación_ing = [[5,1],[2,2],[3,3]]
        

        recorrer_rptas = 0
        puntaje_total = 0
        for i in Ponderación_ing:
            for j in range(i[0]):
                if comparacion_rpta[recorrer_rptas] not in ["-", " "]:
                    puntaje = puntaje * i[1]
                puntaje_total = puntaje_total + puntaje
                recorrer_rptas = recorrer_rptas + 1
                        
        print(dni, tipo_prueba, comparacion_rpta, puntaje_total)
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        
        
        
        
