# algoritmo p resolver un jueguito
#hay n tubos, n-2 colores, 2 tubos vacios iniciales
# 4 pelotas por tubo. Solo se puede mover a vacio o mismo color
# tiene que imprimir los movimientos ganadores
import time as t
import sys
#VARIABLES MANUALES
#ahora, lo mas lento es ingresar a mano la posicion_inicial
posicion_inicial=[[3,7,8,11],[4,6,11,3],[4,3,9,1],[5,10,5,8],[1,4,12,12],[1,11,5,12],[6,6,2,8],[10,10,1,6],[9,3,5,7],[7,2,4,10],[7,11,2,9],[3,9,8,12],[],[]]
espera = 0.2   # para no quemar la maquina

dictColores = {1:'rojo',2:'celeste',3:'azul',4:'ver claro',5:'turq',6:'ver osc',7:'naranja',8:'piel',9:'rosa',10:'blanca',11:'amarilla',12:'violeta'}



#CODIGO
#todos los movimientos posibles en una posicion
ruta=''
n=len(posicion_inicial) #ahora es 14
#una lista con todas las posiciones, para que pueda volver. len es igual a ruta, y movimientos_para_atras puede servir para saber cuanto volver
historial=[posicion_inicial]
posiciones_perdedoras=[]
derivaAperder=[]
dict_pierden={}
movidos=0
proximo_mov=''

#solo podes 'mover' nroid_color_seleccionado a un tubodestino tal que posicion[nro_tuboDestinoPosible]<4 y sea el mismo color o vacio(posicion[m][0]== color or posicion[m]==[]
def listaContiene(list1,list2):
    '''
        check if list1 contains all elements in list2
    '''
    result =  all(elem in list1  for elem in list2)
    if result:
        return True
    else :
        return False

#defino Ganar
listaTubosGanadores=[]
for key in dictColores:
    tuboGanador=[key,key,key,key]
    listaTubosGanadores.append(tuboGanador)


def jugar(posicion):   # no son locales las que estan definidas por primera vez fuera de esto
    pierden_directo=[]
    movidos=0   #movidos en este llamado solo
    perdiste=False
    perdiste_indirecto=False
    nro_tubo=0
    for tuboProv in posicion: #cada tubo proveniente que puede haber. +1 para cuando termino y no encontro nada
        t.sleep(espera) #para no quemar la maquina
        nro_tubo+=1
        print(posicion)
        print('espero')
        if tuboProv==[]: #DecartarTuboVacio, tuboProv
            continue #no tiene sentido elegir un tubo proveniente vacio. Ya se encarga de que el indice 0 este definida
        destinos_malos=[] #junto combinacion proveniente-destino que falla, de un solo proveniente a todo destino
        nroid_color_seleccionado=tuboProv[0]
        nro_tuboDestinoPosible=0
        for tuboDest in posicion:
            nroid_color_destino=0
            nro_tuboDestinoPosible+=1
            #chequeo del movimiento
            condicion_lleno=len(tuboDest)>=4
            if tuboDest!=[]:
                nroid_color_destino=tuboDest[0]
            condicion_distinto_color=nroid_color_destino!=nroid_color_seleccionado and tuboDest!=[]
            condicion_mismo_tubo=tuboProv==tuboDest
            if  condicion_lleno or condicion_mismo_tubo or condicion_distinto_color: #volver todo estructural basico de nuevo, no deberia ser taaaan complejo
                continue
            #encontromov=True
            proximo_mov=str(nro_tubo)+ dictColores.get(nroid_color_seleccionado)+ str(nro_tuboDestinoPosible)+';' #notacion definida

            dict_pierden.setdefault(ruta,[])
            condicion_mov_perdedor=proximo_mov in dict_pierden[ruta] #evaluado luego xq los otros llevan menos calculo p/ descartar(no tiene q pensar el proximo mov)
            if condicion_mov_perdedor:
                continue #asi evito movs que pierden_directo o derivaAperder

            tuboDest.insert(0,nroid_color_seleccionado) #agrega en el tubo destinatario al principio
            tuboProv.pop(0) #borra en el tubo proveniente al principio
            movidos+=1 #del loop
            historial+=posicion   #lo agrega a las posiciones anteriores. Aun asi, cualquier posicion en el historial en un momento podria ser funcion de ruta y pos inicial(contruye esa posicion)
            ruta+=proximo_mov
            print('termino primer for')
            ganaste=listaContiene(posicion,listaTubosGanadores)
            if ganaste:
                print(rut)
                sys.exit()
            break #ya hizo el primer movimiento que encontro, no tiene sentido buscar otro tuboDestino

        if movidos:  #truthey
            break #vuelve a empezar del primer proveniente
        termino_ultimo_tubo=nro_tubo==n+1
        if termino_ultimo_tubo and not movidos:#encontromov
            perdiste=True
        #no_quedan_salidas=? quiza deba definirse antes
        if termino_ultimo_tubo and not movidos and no_quedan_salidas:#ya se sabe que movidos es falso
            perdiste_indirecto=True

    if perdiste:
        dict_pierden[ruta]+=ruta[-1] #lo guardo para evitarlo luego. Pierde directamente
        posicion=historial[-1]
        del ruta[-1]
        jugar_hasta_perder(posicion)  #recursion! mejorarla
    if perdiste_indirecto:
        derivaAperder+=ruta[-1]
        dict_pierden[ruta]+=derivaAperder
        posicion=historial[-1]
        del ruta[-1]

jugar(posicion_inicial) #necesito la recursion, creo. Xq el 'caso base' seria ganar
