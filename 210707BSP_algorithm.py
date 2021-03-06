#python 3.7
#this is the recursive version, soon I'll be uploading better ones(an iterative version, and a more efficient one)
#da los movimientos que ganan un nivel del juego Ball Sort Puzzle (https://play.google.com/store/apps/details?id=com.spicags.ballsort&hl=es_AR&gl=US)


import time as t
import sys, math
#VARIABLES MANUALES
posicion_inicial=[[3,7,8,11],[4,6,11,3],[4,3,9,1],[5,10,5,8],[1,4,12,12],[1,11,5,12],[6,6,2,8],[10,10,1,6],[9,3,5,7],[7,2,4,10],[7,11,2,9],[3,9,8,12],[],[]]
espera = 0.01
dictColores = {1:'rojo',2:'celeste',3:'azul',4:'ver claro',5:'turq',6:'ver osc',7:'naranja',8:'piel',9:'rosa',10:'blanca',11:'amarilla',12:'violeta'}

#CODIGO
ruta=((),())
rutainvertida=((),())
dict_pierden={}
proximo_mov=''
movio=False
n=len(posicion_inicial)
l=len(posicion_inicial[0])
intentos=1 #para debugeo
combis_totales=(len(posicion_inicial)*(len(posicion_inicial)-1))/2
def listaContiene(list1,list2):
    conteo=0
    for element in list2:
        if element in list1: conteo+=1
    estan_todos= conteo==len(list2)
    if estan_todos: return True
    if not estan_todos: return False
listaTubosGanadores=[]
for key in dictColores:
    tuboGanador=[key,key,key,key]
    listaTubosGanadores.append(tuboGanador)
def jugar(posicion,puede_volver):
    global ruta,rutainvertida, intentos
    perdiste=False
    llego_a_ultimoTubo_sin_mover=False
    nro_tubo=0
    while not perdiste:
        nro_tubo=0
        movio=False
        for tuboProv in posicion:
            t.sleep(espera)
            nro_tubo+=1
            if tuboProv==[]: continue
            nroid_color_seleccionado=tuboProv[0]
            nro_tuboDestinoPosible=0
            for tuboDest in posicion:
                nroid_color_destino=0
                nro_tuboDestinoPosible+=1
                condicion_lleno=len(tuboDest)>=4
                if tuboDest!=[]: nroid_color_destino=tuboDest[0]
                condicion_distinto_color=nroid_color_destino!=nroid_color_seleccionado and tuboDest!=[]
                condicion_mismo_tubo=tuboProv==tuboDest
                if  condicion_lleno or condicion_mismo_tubo or condicion_distinto_color: continue
                proximo_mov=str(nro_tubo)+' '+ dictColores.get(nroid_color_seleccionado)+' '+ str(nro_tuboDestinoPosible)
                proximo_mov_numerico=str(nro_tubo)+' '+ str(nroid_color_seleccionado)+' '+ str(nro_tuboDestinoPosible) #para debugeo
                dict_pierden.setdefault(len(ruta),[])
                condicion_mov_perdedor = proximo_mov in dict_pierden[len(ruta)]
                mov_invertido=str(nro_tuboDestinoPosible)+' '+ dictColores.get(nroid_color_seleccionado)+' '+str(nro_tubo)
                condicion_mover_al_reves=proximo_mov in rutainvertida
                if (puede_volver and not condicion_mover_al_reves) or (condicion_mover_al_reves and not puede_volver):
                    continue
                if condicion_mov_perdedor: continue
                if condicion_mover_al_reves:
                    if len(dict_pierden[len(ruta)])>=combis_totales: jugar(posicion,True)
                    listaruta=list(ruta)
                    listaruta.pop(-1)
                    ruta=tuple(listaruta)
                    listarutainv=list(rutainvertida)
                    listarutainv.pop(-1)
                    rutainvertida=tuple(listarutainv)
                    print(posicion) #para debugeo
                    jugar(posicion,False)
                tuboDest.insert(0,nroid_color_seleccionado)
                del tuboProv[0]
                movio=True
                if not condicion_mover_al_reves and not puede_volver:
                    rutainvertida = rutainvertida+(mov_invertido,)
                    ruta= ruta+(proximo_mov,)
                ganaste = listaContiene(posicion,listaTubosGanadores)
                if ganaste:
                    print(ruta)
                    sys.exit()
                break
            if movio: break
            perdiste= nro_tubo==n
            if perdiste: break
        if movio:
            nro_tubo=0
            continue
    if perdiste:
        print(posicion) #para debugeo
        print('intento nro',intentos,'desde',ruta[-1],'fallido') #para debugeo
        intentos+=1
        if ruta[-1] not in rutainvertida: dict_pierden[len(ruta)]+=(ruta[-1], )
        jugar(posicion,True)

jugar(posicion_inicial,False)
