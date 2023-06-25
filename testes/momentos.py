import sys
import os

# Adicione o caminho dos diretórios ao PYTHONPATH
diretorio_entidades = os.path.abspath(os.path.join(os.path.dirname(__file__), '../entidades'))
sys.path.append(diretorio_entidades)
diretorio_vetores = os.path.abspath(os.path.join(os.path.dirname(__file__), '../vetores'))
sys.path.append(diretorio_vetores)

from Forca import Forca
from Ponto import Ponto
from Vetor import Vetor
from Momento import Momento


def teste_momento():
        #teste com inicializacao de momento
        #momento conhecido
        
    momento_a = Momento(5)
    print(momento_a.momento)
        
        #momento desconhecido
    indice_b = 2
    sentido_b = -1
    momento_b = Momento(None, indice_b, sentido_b)
    print(momento_b.indice, momento_b.sentido)
        
        #calcular momento, que recebe forca e ponto e calcula o momento
        
    ponto_a = Ponto(5, 5)
    vetor_a = Vetor(4, 5)
    forca_a = Forca(vetor_a, ponto_a)
    ponto_b = Ponto(0,0)
    momento_c = Momento.calcular_momento(forca_a, ponto_b)
    print(momento_c.momento)
    
    ponto_c = Ponto(-5, 5)
    vetor_c = Vetor(4, 5)
    forca_c = Forca(vetor_c, ponto_c)
    ponto_d = Ponto(0,0)
    momento_d = Momento.calcular_momento(forca_c, ponto_d)
    print(momento_d.momento)
    
    print("Momento de forca desconhecida")
    ponto_e = Ponto(0,0)
    versor_1 = Vetor(1,-1)
    indice_1 = 0
    ponto_f = Ponto(2, 2)
    forca_d = Forca(None,ponto_f, versor_1, indice_1)
    momento_e = Momento.calcular_momento(forca_d, ponto_e)
    print(momento_e)
teste_momento()
       
                 
