 #Mariana Soto Ochoa - Avance del proyecto - A01702593

"""Mi proyecto se trata de determinar la situación financiera de una
empresa y darle recomendaciones. Además el usuario puede decidir si
desea visualizar los índices utilizados para darle recomendaciones
o inclusive ver los reportes financieros (balance y estado de
resultados."""

"""Algoritmo

EO(ventas_totales,costo_ventas,gastos,intereses,impuestos,activo_fijo,
activo_circulante,pasivo circulante,pasivo fijo,almacen)

se importa turtle

utilidad_bruta(ventas_totales,costo_ventas,gastos)
    regresa(ventas_totales-costo_ventas-gastos)

utilidad_neta (utilidad_bruta,intereses,impuestos)
    regresa(utilidad_bruta-intereses-impuestos)

capital (activo_circulante,activo_fijo,pasivo_circulante,pasivo_fijo):
    regresa(activo_circulante+activo_fijo-pasivo_circulante-pasivo_fijo)

i_utilidad_neta(ut_neta, ventas_totales)
    res = (ut_neta/ventas_totales)*100
    regresa(res)

i_liquidez (activo_circulante,pasivo_circulante)
    regresa(activo_circulante/pasivo_circulante)

i_liquidez_acida (activo_circulante,almacen,pasivo_circulante)
    regresa((activo_circulante-almacen)/pasivo_circulante)

i_retorno_capital (ut_neta, capital)
    return((utilidad_neta/capital)*100)

comentarios_indices(i_utilidad_neta,i_liquidez,i_liquidez_acida,
                        i_retorno_capital):
    archivo = abrir archivo
    lineas = leer lineas de archivo
    cerrar archivo
    matriz = []
    por cada linea:
        lista = []
        line = separar linea
        por cada elemento en line:
            insertar elemento en lista
        insertar lista en matriz
    
    por cada valor de entrada existen las condiciones siguientes en este orden
        i_utilidad_neta >= 35
        otro valor de i_utilidad_neta
        1>= i_liquidez and i_liquidez <=2
        i_liquidez < 1
        i_liquidez > 1
        i_liquidez_acida >1
        i_liquidez_acida <1
        i_liquidez_acida == 1
        i_retorno_capital > 8
        otro valor de i_retorno_capital
        si la condicion se cumple
            se busca el valor de la matriz que le pertenece
                matriz [0 al 9][1]
            se le asigna una variable comentario_entrada

    lista_comentarios = [comentario_utilidad,comentario_liquidez,
                         comentario_acida,comentario_capital]
    comentarios_string = lista_comentarios a string
    regresa(comentarios_string)

alinear_izquierda()
    subir cursor
    girar 143 a la izquierda
    avanzar 565
    bajar cursor

cambiar_angulo_avanzar(izquierda, derecha, avanzar)
    subir cursor
    girar a la izquierda
    girar a la derecha
    avanzar
    bajar cursor

trazar_linea(izquierda, derecha, avanzar)
    girar a la izquierda
    girar a la derecha
    avanzar

trazar_larga_regresar()
    trazar_linea(90,0,875)
    cambiar_angulo_avanzar(0, 180, 875)
    cambiar_angulo_avanzar(90, 0, 50)

graficar_activo_pasivo(titulos_balance, subtitulos_balance,
                           valores_balance)
    por cada titulo_balance
        escribir el titulo_balance
        trazar_larga_regresar()
        en un rango del 0 al 3
            escribir subtitulo_balance con indice de contador
            trazar_linea(90,0,400)
            escribir valores_balance con indice de contador
            cambiar_angulo_avanzar(180, 0, 400)
            cambiar_angulo_avanzar(90, 0, 50)


graficar_capital(capital)
    Escribir capital
    trazar_larga_regresar()
    escribir comentario
    trazar_linea(90,0,400)
    escribir valor del capital
    cambiar_angulo_avanzar(180, 0, 400)
    cambiar_angulo_avanzar(90, 0, 50)

balance()
    alinear_izquierda()
    cambiar_angulo_avanzar(0, 53, 10)
    escribir balance
    cambiar_angulo_avanzar(180, 0, 10)
    trazar_larga_regresar()
    graficar_activo_pasivo(titulos_balance, subtitulos_balance,
                           valores_balance)
    graficar_capital(capital)


estado_resultados(subtitulos_estado, valores_estado)
    alinear_izquierda()
    cambiar_angulo_avanzar(0, 53, 10)
    escribir estado de resultados
    cambiar_angulo_avanzar(180, 0, 10)
    trazar_larga_regresar()
    por cada sutitulos_estado
        escribir subtitulo_estado con el indice del contador
        trazar_linea(90,0,400)
        escribir valor_estado con el indice del contador
        cambiar_angulo_avanzar(180, 0, 400)
        cambiar_angulo_avanzar(90, 0, 50)

limpia_cadena(caracteres_seguros, string)
    nueva_string = []
    si string no esta completamente en mayusculas
        string = string en minusculas
    por cada letra en string
        si la letra esta caracteres_seguros:
            insertar letra en nueva_string
    regresa(nueva_string convertida a string)

imprimir_input_usuario(string, lista)
    si string tiene un nombre entre varios nombres
        res = posicion en lista seleccionado para ese nombre
    de otra manera
        res = "no reconocido"
    si string no esta entre los nombres
        string = False

MAIN

ventana_emergente con turtle
acelerar velocidad de turtle

i_utilidad_neta = i_utilidad_neta(ut_neta, ventas_totales))
i_liquidez = i_liquidez(activo_circulante,pasivo_circulante))
i_liquidez_acida = i_liquidez_acida(activo_circulante,almacen,pasivo_circulante)
i_retorno_capital = i_retorno_capital(ut_neta,capital)
lista = [['-La utilidad neta es: ', i_utilidad_neta],
         ['-La liquidez es: ', i_liquidez],
         ['-La liquidez ácida es: ', i_liquidez_acida],
         ['-El RCI es: ', i_retorno_capital]]
titulos_balance = ["Activo", "Pasivo"]
subtitulos_balance = ["Activo circulante", "Activo fijo", "Activo total",
                      "Pasivo circulante","Pasivo fijo", "Pasivo total"]
valores_balance = [activo_circulante, activo_fijo,
                   activo_circulante + activo_fijo,
                   pasivo_circulante, pasivo_fijo,
                   pasivo_circulante + pasivo_fijo]
subtitulos_estado = ["Ventas totales", "Costo de ventas", "Gastos",
                     "Utilidad bruta", "Intereses", "Impuestos",
                     "Utilidad neta"] 
valores_estado = [ventas_totales, costo_ventas, gastos,
           utilidad_bruta,intereses, impuestos, utilidad_neta]



comentar_indices = comentarios_indices(i_utilidad_neta,i_liquidez,
                                  i_liquidez_acida,i_retorno_capital),

caracteres_seguros = "aábcdefghijklmnopqrstuvwxyz"
indice = True
mientras que indice = True
    se abre archivo
    se escribe lo que hay en archivo
    string = limpia_cadena(caracteres_seguros, string)
    imprimir balance o estado
    si res != balance o estado
        se borra la pantalla
        se acelera turtle
        alinear_izquierda()
        cambiar_angulo_avanzar(0, 233, 500)
        cambiar_angulo_avanzar(90, 0, 200)
        se imprime res



EF(i_utilidad_neta, i_liquidez,
i_liquidez_acida, i_retorno_capital, balance, estado_resultados)
"""
import turtle

"""Las funciones de utilidad bruta y la utilidad neta contienen
todos los datos para realizar un balance financiero"""

def utilidad_bruta(ventas_totales,costo_ventas,gastos):
    #La funcion le resta los gastos y costo de ventas a las ventas totales
    return(float(ventas_totales)-float(costo_ventas)-float(gastos))
"""
#Prueba 1
contar = 0
if utilidad_bruta(20,10,5) == 5:
    contar += 1
if utilidad_bruta(10,50,35.5) == -75.5:
    contar += 1
if utilidad_bruta(-10,20.78,37) == -67.78:
    contar += 1
if utilidad_bruta(-87.34,-24,-190) == 126.66:
    contar += 1
if utilidad_bruta(0,0,0) == 0:
    contar += 1
print(contar, "de 5 pruebas fueron exitosas")
"""

def utilidad_neta (ut_bruta,intereses,impuestos):
    #La funcion le resta los intereses e impuestos a la utilidad bruta
    return(ut_bruta-float(intereses)-float(impuestos))
"""
#Prueba 2
contar = 0
if utilidad_neta(20,10,5) == 5:
    contar += 1
if utilidad_neta(10,50,35.5) == -75.5:
    contar += 1
if utilidad_neta(-10,20.78,37) == -67.78:
    contar += 1
if utilidad_neta(-87.34,-24,-190) == 126.66:
    contar += 1
print(contar, "de 4 pruebas fueron exitosas")
"""


def capital (activo_circulante,activo_fijo,pasivo_circulante,pasivo_fijo):
    #La funcion suma los activos totales y les resta los pasivos totales
    #Esta función contiene todos los datos para hacer un balance financiero
    return (activo_circulante+activo_fijo-pasivo_circulante-pasivo_fijo)
"""
#Prueba 3
contar = 0
if capital(20,10,5,13) == 12:
    contar += 1
if capital(10,27.9,50,35.5) == -47.6:
    contar += 1
if capital(-87.34,-24,-190,-90) == 168.66:
    contar += 1
print(contar, "de 3 pruebas fueron exitosas")
"""

"""Las funciones que comienzan por "i_" son indices financieros
en base al estado de resultados y el balance"""

def i_utilidad_neta (ut_neta, ventas_totales):
    """La funcion divide la utilidad neta entre las
    ventas totales y multiplica esto por 100"""
    res = (ut_neta/ventas_totales)*100
    return(res)

"""
#Prueba 4
#No puede haber división entre 0 porque
#hay un parámetro en el input que lo impide
contar = 0
if i_utilidad_neta(20,10) == 200:
    contar += 1
if i_utilidad_neta(27.5,27.5) == 100:
    contar += 1
if i_utilidad_neta(2,0.5) == 400:
    contar += 1
if i_utilidad_neta(-3,2) == -150:
    contar += 1
if i_utilidad_neta(-3,-2) == 150:
    contar += 1
print(contar, "de 5 pruebas fueron exitosas")
"""

def i_liquidez (activo_circulante,pasivo_circulante):
    #La función divide el activo circulante entre el pasivo circulante
    return(activo_circulante/pasivo_circulante)
"""
#Prueba 5
#No puede haber división entre 0
#porque el parámetro en input lo impide
contar = 0
if i_liquidez(20,10) == 2:
    contar += 1
if i_liquidez(27.5,27.5) == 1:
    contar += 1
if i_liquidez(2,0.5) == 4:
    contar += 1
if i_liquidez(-3,2) == -1.5:
    contar += 1
if i_liquidez(-3,-2) == 1.5:
    contar += 1
print(contar, "de 5 pruebas fueron exitosas")
"""

def i_liquidez_acida (activo_circulante,almacen,pasivo_circulante):
    """Esta funcion le resta el almacen al activo circulante y
        divide el resultante entre el pasivo circulante"""
    return((activo_circulante-almacen)/pasivo_circulante)
"""
#Prueba 6
#No puede haber división entre 0
#porque el parámetro en input lo impide
contar = 0
if i_liquidez_acida(40,20,10) == 2:
    contar += 1
if i_liquidez_acida(30,2.5,27.5) == 1:
    contar += 1
if i_liquidez_acida(5,3,0.5) == 4:
    contar += 1
if i_liquidez_acida(6,9,2) == -1.5:
    contar += 1
if i_liquidez_acida(9,12,-2) == 1.5:
    contar += 1
print(contar, "de 5 pruebas fueron exitosas")
"""

def i_retorno_capital (ut_neta, capital):
    """Esta funcion divide la utilidad bruta entre
        el capital y multiplica el resultante por 100"""
    #La función regresa el retorno sobre el capital invertido o RCI
    return((ut_neta/capital)*100)

"""
#Prueba 7
#No puede haber división entre 0 porque
#hay un parámetro en input que lo impide
contar = 0
if i_retorno_capital(20,10) == 200:
    contar += 1
if i_retorno_capital(27.5,27.5) == 100:
    contar += 1
if i_retorno_capital(2,0.5) == 400:
    contar += 1
if i_retorno_capital(-3,2) == -150:
    contar += 1
if i_retorno_capital(-3,-2) == 150:
    contar += 1
print(contar, "de 5 pruebas fueron exitosas")
"""

def comentarios_indices(i_utilidad_neta,i_liquidez,i_liquidez_acida,
                        i_retorno_capital):
    """Se define una función que decida qué tan eficaz es el
        funcionamiento de la empresa"""
    #Se abre un archivo con todos los comentarios
    archivo = open("archivo_indices.txt","r")
    lineas = archivo.readlines()
    archivo.close()
    matriz = []
    for line in lineas:
        lista = []
        line = line.split("\t")
        for j in line:
            lista.append(j)
        matriz.append(lista)
    
    if (i_utilidad_neta >= 35):
        comentario_utilidad = matriz [0][1]
    else:
        comentario_utilidad = matriz [1][1]
    if (1>= i_liquidez and i_liquidez <=2):
        comentario_liquidez = matriz [2][1]
    elif (i_liquidez < 1):
        comentario_liquidez = matriz [3][1]
    elif (i_liquidez > 1):
        comentario_liquidez = matriz [4][1]
    if (i_liquidez_acida >1):
        comentario_acida = matriz [5][1]
    elif (i_liquidez_acida <1):
        comentario_acida = matriz [6][1]
    elif (i_liquidez_acida == 1):
        comentario_acida = matriz [7][1]
    if (i_retorno_capital > 8):
        comentario_capital = matriz [8][1]
    else:
        comentario_capital = matriz [9][1]
    #Lista para agrupar los comentarios de los índices
    lista_comentarios = [comentario_utilidad,comentario_liquidez,
                         comentario_acida,comentario_capital]
    #Se fusiona la lista para que al imprimirla no aparezcan comas ni comillas
    comentarios_string = "".join(lista_comentarios)
    return (comentarios_string)

def alinear_izquierda():
    #Función que dirige al cursor a la esquina superior izquierda
    turtle.penup() #Se esconde el cursor de turtle
    turtle.left(143) #Se cambia el angulo de la flecha que va a dibujar
    turtle.forward(565) #La flecha avanza sin dejar rastro
    turtle.pendown() #Baja el cursor para poder escribir

def cambiar_angulo_avanzar(izquierda, derecha, avanzar):
    #Función que gira el cursor y avanza el cursor de turtle
    turtle.penup()
    turtle.left(izquierda)
    turtle.right(derecha)
    turtle.forward(avanzar)
    turtle.pendown()

def trazar_linea(izquierda, derecha, avanzar):
    #Función que gira el cursor y avanza el cursor dejando rastro
    turtle.left(izquierda)
    turtle.right(derecha)
    turtle.forward(avanzar)


def trazar_larga_regresar():
    """Función que traza una línea, regresa,
        gira 90 grados y avanza sin dejar rastro"""
    trazar_linea(90,0,875)
    cambiar_angulo_avanzar(0, 180, 875)
    cambiar_angulo_avanzar(90, 0, 50)

def graficar_activo_pasivo(titulos_balance, subtitulos_balance,
                           valores_balance):
    #Función que dibuja el activo y el pasivo del balance
    cont_1 = 0
    cont_2 = 0
    for i in titulos_balance:
        turtle.write(titulos_balance[cont_1], font=("Arial", 12, "normal"))
        trazar_larga_regresar()
        for j in range (3):
            turtle.write(subtitulos_balance[cont_2])
            trazar_linea(90,0,400)
            turtle.write(valores_balance[cont_2])
            cambiar_angulo_avanzar(180, 0, 400)
            cambiar_angulo_avanzar(90, 0, 50)
            cont_2 += 1
        cont_1 += 1

def graficar_capital(capital):
    #Función que dibuja el capital del balance
    turtle.write(("Capital"), font=("Arial", 12, "normal"))
    trazar_larga_regresar()
    turtle.write("Recuerda que el capital es activo total-pasivo total")
    trazar_linea(90,0,400)
    turtle.write(capital)
    cambiar_angulo_avanzar(180, 0, 400)
    cambiar_angulo_avanzar(90, 0, 50)

def balance():
    #Función que dibuja todo el balance
    alinear_izquierda()
    cambiar_angulo_avanzar(0, 53, 10)
    turtle.write("Balance", font=("Arial", 25, "normal"))
    cambiar_angulo_avanzar(180, 0, 10)
    trazar_larga_regresar()
    graficar_activo_pasivo(titulos_balance, subtitulos_balance,
                           valores_balance)
    graficar_capital(capital)


def estado_resultados(subtitulos_estado, valores_estado):
    #Función que dibuja el estado de resultados
    alinear_izquierda()
    cambiar_angulo_avanzar(0, 53, 10)
    turtle.write("Estado de resultados", font=("Arial", 25, "normal"))
    cambiar_angulo_avanzar(180, 0, 10)
    trazar_larga_regresar()
    cont = 0
    for j in subtitulos_estado:
        turtle.write(subtitulos_estado[cont])
        trazar_linea(90,0,400)
        turtle.write(valores_estado[cont])
        cambiar_angulo_avanzar(180, 0, 400)
        cambiar_angulo_avanzar(90, 0, 50)
        cont += 1

def limpia_cadena(caracteres_seguros, string):
    """Función para sustituir los datos inválidos del
        string que el usuario introduce cuando quiere ver un valor"""
    nueva_string = []
    if string.islower() == False: #Reconoce si una palabra está en mayúsculas
        string = string.lower() #Si está en mayúsculas lo cambia a minúscilas
    for letra in string:
        if letra in caracteres_seguros:
            nueva_string.append(letra) #Lista con caracteres válidos
    return ("".join(nueva_string))

def imprimir_input_usuario(string, lista):
    #Función que reconoce lo que el usuario pide y lo regresa
    if string == ("utilidadneta"):
        res = (lista[0][0], lista[0][1])
    elif string == ("liquidez"):
        res = (lista[1][0], lista[1][1])
    elif string == ("liquidezácida") or string == ("liquidezacida") :
        res = (lista[2][0], lista[2][1])
    elif string == ("rci"):
        res = (lista[3][0], lista[3][1])
    elif string == ("imprimirtodos"):
        res = []
        cambiar_angulo_avanzar(0, 0, 100)
        for row in lista:
            cont = 1
            for elem in row:
                res.append(elem)
                if cont%2 == 0:
                     res.append("\n")
                cont += 1
    elif string == ("fin"):
        res= ("")
        indice = False
    elif string == ("balance"):
        res = ("balance")
        turtle.clearscreen()
        turtle.speed(0)
        balance()
    elif string == ("estadoderesultados"):
        res = ("estadoderesultados")
        turtle.clearscreen()
        turtle.speed(0)
        estado_resultados(subtitulos_estado, valores_estado)
    else:
        res = ("Nombre no reconocido")
    return ("".join(res))


#Valores de entrada para el estado de resultados
ventana_emergente = turtle.Screen()
turtle.speed(0)

ventas_totales = float(turtle.numinput("Ventas","Escribe las ventas totales",
                                       0,1,9000000000000))
costo_ventas= float(turtle.numinput("Costo de ventas",
            "Escribe el costo de ventas",0,1,9000000000000))
gastos= float(turtle.numinput("Gastos","Escribe los gastos",
                              0,1,9000000000000))
intereses= float(turtle.numinput("Intereses","Escribe los intereses",
                                 0,1,9000000000000))
impuestos= float(turtle.numinput("Impuestos","Escribe los impuestos",
                                 0,1,9000000000000))

#Valores de entrada para el balance
almacen= float(turtle.numinput("Almacen","Escribe el valor del almacen",
                               0,1,9000000000000))
activo_circulante= float(turtle.numinput("Act.",
                    "Escribe los activos circulantes",0,1,9000000000000))
activo_fijo= float(turtle.numinput("Activos fijos",
            "Escribe los activos fijos",0,1,9000000000000))
pasivo_circulante= float(turtle.numinput("Deudas",
                    "Escribe las deudas circulantes",0,1,9000000000000))
pasivo_fijo= float(turtle.numinput("Deudas",
                "Escribe las deudas a largo plazo",0,1,9000000000000))

#Valores de salida
ut_bruta = utilidad_bruta(ventas_totales,costo_ventas,gastos)
ut_neta = utilidad_neta (ut_bruta,intereses,impuestos)
capital = capital(activo_circulante,activo_fijo,pasivo_circulante,pasivo_fijo)
i_utilidad_neta=float("%.2f" % (i_utilidad_neta(ut_neta, ventas_totales)))
i_liquidez=float("%.2f" % (i_liquidez(activo_circulante,pasivo_circulante)))
i_liquidez_acida=float("%.2f" % (i_liquidez_acida(activo_circulante,almacen,
pasivo_circulante)))
i_retorno_capital=float("%.2f" % (i_retorno_capital(ut_neta,capital)))
lista = [['-La utilidad neta es: ',str(i_utilidad_neta)],
         ['-La liquidez es: ',str(i_liquidez)],
         ['-La liquidez ácida es: ',str(i_liquidez_acida)],
         ['-El RCI es: ',str(i_retorno_capital)]]
titulos_balance = ["Activo", "Pasivo"]
subtitulos_balance = ["Activo circulante", "Activo fijo", "Activo total",
                      "Pasivo circulante","Pasivo fijo", "Pasivo total"]
valores_balance = [activo_circulante, activo_fijo,
                   activo_circulante + activo_fijo,
                   pasivo_circulante, pasivo_fijo,
                   pasivo_circulante + pasivo_fijo]
subtitulos_estado = ["Ventas totales", "Costo de ventas", "Gastos",
                     "Utilidad bruta", "Intereses", "Impuestos",
                     "Utilidad neta"] 
valores_estado = [ventas_totales, costo_ventas, gastos,
           ut_bruta,intereses, impuestos, ut_neta]

#Comentario para la empresa en relación a los índices obtenidos
style = ('Comic Sans',20,'italic')
alinear_izquierda()
turtle.write ("ANÁLISIS DE ÍNDICES", font=("Arial", 25, "normal"))
cambiar_angulo_avanzar(130, 0, 500)
comentar_indices = turtle.write (comentarios_indices
                                 (i_utilidad_neta,i_liquidez,
                                  i_liquidez_acida,i_retorno_capital),
                font=('Comic Sans',12,'italic'))

#Para imprimir los valores que el usuario quiera conocer
caracteres_seguros = "aábcdefghijklmnopqrstuvwxyz"
indice = True
while indice == True: #Ciclo con inputs hasta que el usuario escriba FIN
    archivo_2 = open("archivo_indices_2.txt","r")
    contenido = archivo_2.read()
    archivo_2.close()
    string = turtle.textinput("ÍNDICES",contenido)
    string = limpia_cadena(caracteres_seguros, string)
    res = imprimir_input_usuario(string,lista)
    if res != ("balance") and res != ("estadoderesultados"):
        turtle.clearscreen()
        turtle.speed(0)
        alinear_izquierda()
        cambiar_angulo_avanzar(0, 233, 500)
        cambiar_angulo_avanzar(90, 0, 200)
        turtle.write(res,font=('Comic Sans',12,'italic' ))
