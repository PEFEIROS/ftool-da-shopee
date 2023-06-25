###n usaremos, por hora
import math
import numpy as np
#recebe as listas de corpos e interacoes conhecidas e monta equacoes de coisas conhecidas
def CalculaReacoes (listaDeCorpos, forcasConhecidasX, forcasConhecidasY, momentosConhecidosM):
    
    for forcax in forcasConhecidasX:
        SomaX += forcax
    
    for forcay in forcasConhecidasY:
        SomaY += forcay

    for momento in momentosConhecidosM:
        SomaM += momento

    for corpo in listaDeCorpos:
        EquacaoX = []
        EquacaoY = []
        EquacaoM = []
        #monta o vetor de incognitas das reações em x
        if(corpo.tipo == "Apoio Duplo"):
            EquacaoX.append(1)
            EquacaoX.append(0)
        if(corpo.tipo == "Engaste"):
            EquacaoX.append(1)
            EquacaoX.append(0)
            EquacaoX.append(0)
        if(corpo.tipo == "Apoio Simples"):
            EquacaoX.append(0)
        #monta o vetor de incognitas das reações em y
        if(corpo.tipo == "Apoio Duplo"): #Fx, Fy
            EquacaoY.append(0)
            EquacaoY.append(1)
        if(corpo.tipo == "Engaste"): #Fx, Fy, M
            EquacaoY.append(0)
            EquacaoY.append(1)
            EquacaoY.append(0)
        if(corpo.tipo == "Apoio Simples"):
            EquacaoY.append(1)
        #monta o vetor de incognitas das reacoes de momento m
        #if(corpo.tipo == "Apoio Duplo"):
        #    EquacaoM.append(-(corpo.forca.y))
        #    EquacaoM.append(corpo.forca.x)
        #if(corpo.tipo == "Engaste"):
        #    EquacaoM.append(-(corpo.forca.y))
        #    EquacaoM.append(corpo.forca.y)
        #    EquacaoM.append(1)
        #else
        #    EquacaoM.append(0)

        #monta o vetor de incognitas das reacoes de momento m
        #distX = abs(listaDeCorpos[0].referencial.x - corpo.referencial.x)
        #distY = abs(listaDeCorpos[0].referencial.y - corpo.referencial.y)
        #if(corpo.tipo == "Apoio Duplo"):
        #    EquacaoM.append(distY)
        #    EquacaoM.append(distX)
        #if(corpo.tipo == "Engaste"):
        #    EquacaoM.append(distY)
        #    EquacaoM.append(distX)
        #    EquacaoM.append(1)
        #if(corpo.tipo == "Apoio Simples"):
        #    EquacaoM.append(0) 
        
        #monta o vetor de incognitas do momento
                        #calcula a distancia até a origem (1° elemento do vetor)
        dist = math.sqrt((listaDeCorpos[0].referencial.x-corpo.referencial.x)**2 + (listaDeCorpos(0).referencial.y-corpo.referencial.y)**2)
        if(corpo.tipo == "Apoio Duplo"): #Fx, Fy
            EquacaoM.append(0)
            EquacaoM.append(dist)
        if(corpo.tipo == "Engaste"): #Fx, Fy, M
            EquacaoM.append(0)
            EquacaoM.append(dist)
            EquacaoM.append(1)
        if(corpo.tipo == "Apoio Simples"): #Fy
            EquacaoM.append(dist)
    coeficientes = np.array([EquacaoX, EquacaoY, EquacaoM])
    constantes = np.array([-SomaX, -SomaY, -SomaM])
    np.linalg.solve(coeficientes, constantes)
    




