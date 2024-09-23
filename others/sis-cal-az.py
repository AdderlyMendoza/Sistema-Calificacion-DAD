archivoIdentificacion = 'az4id.dat'
archivoRespuestas = 'az4re.dat'

datosHojaIdentificacion = []
datosHojaRespuestas = []


# Extraemos datos de Identifación
with open(archivoIdentificacion, 'r') as idenArchivo:
    idenLineas = idenArchivo.readlines()  # Lee todas las líneas y las guarda en una lista
    for linea in idenLineas[:-1]:
        # Extraer los 4 datos específicos
        idenIdentificacion = linea[0:21].strip()         
        idenDato01 = linea[24:28].strip()        
        idenDato02 = linea[29:34].strip()         
        idenDato03 = linea[38].strip()            
        idenDNI = linea[40:].strip()         


        datosHojaIdentificacion.append([idenIdentificacion, idenDato01, idenDato02, idenDato03, idenDNI])
        

# Extraemos datos de Respuestas   
with open(archivoRespuestas, 'r') as resArchivo:
    resLineas = resArchivo.readlines()  # Lee todas las líneas y las guarda en una lista
    for linea in resLineas[:-1]:
        # Extraer los 4 datos específicos
        resIdentificacion = linea[0:21].strip()          
        resDato01 = linea[24:28].strip()       
        resDato02 = linea[29:34].strip()         
        resDato03 = linea[38].strip()           
        resRespuestas = linea[40:].strip()          

        datosHojaRespuestas.append([resIdentificacion, resDato01, resDato02, resDato03, resRespuestas])

# Comparamos datos y extraemos DNI, TIPO DE PRUEBA res e iden y RESPUESTAS
dniPostulante = ""
idenTipoPruebaPostulante= ""
resTipoPruebaPostulante= ""
respuestasPostulante = "" 
datosFinales = []
for i, j in zip(datosHojaIdentificacion, datosHojaRespuestas):
    if ( i[0][3:] == j[0][3:] ): # comparamos identificadores en ambos .dat
        # Manejo de errores
        # if ( len(i[4]) == 15  ):
        if( len(i[4][7:]) >= 8 ): # num caracteres DNI
            dniPostulante = i[4][7:15]
        else:
            dniPostulante = "errorDNI"

        # Tipo de prueba HOJA IDENTIFICACION
        if( len(i[4]) > 6 ):
            if ( i[4][6] in ['P','Q','R','S','T'] ):
                idenTipoPruebaPostulante = i[4][6] 
            else:
                idenTipoPruebaPostulante = "error"
        else:
            idenTipoPruebaPostulante = "error"
        
        # Tipo de prueba HOJA RESPUESTAS
        if( len(j[4]) > 6 ):
            if ( j[4][6] in ['P','Q','R','S','T'] ):
                resTipoPruebaPostulante = j[4][6] 
            else:
                resTipoPruebaPostulante = "error"
        else:
            resTipoPruebaPostulante = "error"
        
        respuestasPostulante = j[4][7:]
        datosFinales.append([dniPostulante, idenTipoPruebaPostulante, resTipoPruebaPostulante, respuestasPostulante])
        
        dniPostulante = ""
        tipoPruebaPostulante= ""
        respuestasPostulante = "" 
        
        
# Sacamos respuestas correctas
respuestas_P = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
respuestas_Q = "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB"
respuestas_R = "CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC"
respuestas_S = "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD"
respuestas_T = "EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE"
rptaFijas = ""

respuestasCorrectasPostu = []
rptCorrecta = []

for i in datosFinales:
    if( i[1] == "P" ): # Tomando TP de HOJA IDENTIFICACION
        rptaFijas = respuestas_P
    if( i[1] == "Q" ):
        rptaFijas = respuestas_Q
    if( i[1] == "R" ):
        rptaFijas = respuestas_R
    if( i[1] == "S" ):
        rptaFijas = respuestas_S
    if( i[1] == "T" ):
        rptaFijas = respuestas_T
    
    if( len(i[3]) < 61): # si hay menos de 60 respuestas (no marco las últimas xd)
        for p in range(61-len(i[3])):
            i[3] = i[3] + "-"
    
    for rPostu, rFijas in zip(i[3],rptaFijas):
        if(rPostu == rFijas):
            rptCorrecta.append(rPostu)
        else:
            rptCorrecta.append("-")
    
    respuestasCorrectasPostu.append(rptCorrecta)
    rptCorrecta = []
    
# Sacamos nota final

ponderacionIng = [[4,5.201],
                  [4,5.202],
                  [4,5.303],
                  [4,5.404],
                  [4,5.905],
                  [4,5.406],
                  [2,3.177],
                  [4,3.802],
                  [2,2.576],
                  [2,3.701],
                  [2,3.101],
                  [2,3.502],
                  [4,3.352],
                  [2,2.501],
                  [6,7.603],
                  [6,7.103],
                  [2,4.087],
                  [2,4.087]]

recorrerRptas = 0
puntajeTotal = 0 # puntaje del postulante
x = 0 # recorrer las respuestas del postulante
recorrerPostulantes = 0

for i in respuestasCorrectasPostu:
    for j in ponderacionIng:
        for k in range(j[0]):
            if i[x] is not "-":
                puntaje = 10 * j[1]
                puntajeTotal = puntajeTotal + puntaje 
            x = x + 1
            
    datosFinales[recorrerPostulantes].append(puntajeTotal)
    print(datosFinales[recorrerPostulantes])
    x = 0 # reiniciamos
    recorrerPostulantes = recorrerPostulantes + 1
    puntajeTotal = 0


# Exportar a Excel
import pandas as pd
# Convertir el array en un DataFrame
df = pd.DataFrame(datosFinales, columns=['DNI', 'TP. IDEN', 'TP. RES', 'RESPUESTAS', 'PUNTAJE'])
        
df.to_excel('reporteFinal.xlsx', index=False)

    
        
    
    

    