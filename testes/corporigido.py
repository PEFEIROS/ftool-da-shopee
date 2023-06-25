import sys
import os

# Adicione o caminho dos diretórios ao PYTHONPATH
diretorio_vetorORponto = os.path.abspath(os.path.join(os.path.dirname(__file__), '../vetores'))
sys.path.append(diretorio_vetorORponto)

from Ponto import Ponto
from Vetor import Vetor

# Adicione o caminho dos diretórios ao PYTHONPATH
diretorio_Forca = os.path.abspath(os.path.join(os.path.dirname(__file__), '../entidades'))
sys.path.append(diretorio_Forca)

from Forca import Forca
from Momento import Momento

# Adicione o caminho dos diretórios ao PYTHONPATH
diretorio_Corpo = os.path.abspath(os.path.join(os.path.dirname(__file__), '../corpos'))
sys.path.append(diretorio_Corpo)

from CorpoRigido import CorpoRigido

#TESTE DO PRINTA CORPO
def printaCorpo (corpo):
    print(corpo.tipo)
    print("lista de forcas")
    i = 0
    #printa a lista de forcas
    for forca in corpo.lista_forcas:
        print("forca[", i, "] = (", forca.vetor.x, ",", forca.vetor.y, ")")
        i = i + 1
    print("\n")

    #printa a lista de momentos
    print("lista de momentos")
    i = 0
    for momento in corpo.lista_momentos:
        if(momento.incognita):
            print("momento[", i, "] - indice = ", momento.indice, "; sentido = ", momento.sentido)
        else:
            print("momento[", i, "] = ", momento)
        i = i + 1
    print("\n")
    
    
    #printa a lista de cortes
    i = 0
    print("lista de cortes")
    for corte in corpo.lista_cortes:
        print("corte[", i, "] = (", corte.x, ",", corte.y, ")")
        i = i + 1
    print("\n")


corpo1 = CorpoRigido("BARRA")
ponto1 = Ponto(5, 5)
vetor1 = Vetor(4, 5)
forca1 = Forca(vetor1, ponto1)
corpo1.adicionar_forca(forca1) 
momento1 = Momento(None, 1, 1)
corpo1.adicionar_momento(momento1)

ponto2 = Ponto(7, 7)
vetor2 = Vetor(7, 7)
forca2 = Forca(vetor2, ponto2)
corpo1.adicionar_forca(forca2) 
printaCorpo(corpo1)
