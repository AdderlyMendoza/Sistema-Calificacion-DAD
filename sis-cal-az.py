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

        # Imprimir los valores extraídos
        # print(idenIdentificacion, idenDato01, idenDato02, idenDato03, idenDNI)
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

        # Imprimir los valores extraídos
        # print(resIdentificacion, resDato01, resDato02, resDato03, resRespuestas)
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
        
        # print("DNI:", dniPostulante, ", idenTP:", idenTipoPruebaPostulante, "resTP:", resTipoPruebaPostulante,  ", RESPUESTAS:", respuestasPostulante)

        dniPostulante = ""
        tipoPruebaPostulante= ""
        respuestasPostulante = "" 
        
        

# Sacamos nota final
respuestas_P = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
respuestas_Q = "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB"
respuestas_R = "CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC"
respuestas_S = "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD"
respuestas_T = "EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE"
rptaFijas = ""

for i in datosFinales:
    if( datosFinales[1] == "P" ): # Tomando TP de HOJA IDENTIFICACION
        rptaFijas = "P"
    if( datosFinales[1] == "Q" ):
        rptaFijas = "Q"
    if( datosFinales[1] == "R" ):
        rptaFijas = "R"
    if( datosFinales[1] == "S" ):
        rptaFijas = "S"
    if( datosFinales[1] == "T" ):
        rptaFijas = "T"
    
    

    