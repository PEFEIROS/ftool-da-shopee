### por hora não usaremos
import sys
import os

# Adicione o caminho dos diretórios ao PYTHONPATH
diretorio_entidades = os.path.abspath(os.path.join(os.path.dirname(__file__), '../entidades'))
sys.path.append(diretorio_entidades)
diretorio_vetores = os.path.abspath(os.path.join(os.path.dirname(__file__), '../vetores'))
sys.path.append(diretorio_vetores)
diretorio_corpos = os.path.abspath(os.path.join(os.path.dirname(__file__), '../corpos'))
sys.path.append(diretorio_corpos)
diretorio_resolutor = os.path.abspath(os.path.join(os.path.dirname(__file__), '../resolutor'))
sys.path.append(diretorio_resolutor)

from CorpoRigido import CorpoRigido
from Forca import Forca
from Ponto import Ponto
from Vetor import Vetor
from Resolutor import Resolutor
from Momento import Momento
from Vinculo import Vinculo

#momentos desconhecidos:
#sentido-> dado por nos como positivo -> o indice eh dado no backend
#forcas desconhecidas:
#None, ponto, versor. -> o indice eh dado no backend

class MontadorDeIncognitas:
    #recebe os vinculos e transforma em incognita
    def __init__ (self):
        self.indice_incognitas = 0
        
    def IncognitasCompleto(self, lista_de_corpos, lista_de_vinculos): #cada vinculo tem uma lista em que há 2 numeros, eses numeros indicam
        for vinculo in lista_de_vinculos:                               #o indice das barras que sofrem a aplicação do vinculo na lista_de_corpos
                if (vinculo.tipo == "Apoio Duplo"): 
                    for corpo in vinculo.lista_corpos:
                        if(corpo == vinculo.lista_corpos[0]):
                            lista_de_corpos[corpo].adicionar_forca(Forca(None, vinculo.posicao, Vetor(1,0), self.indice_incognitas))#0
                            lista_de_corpos[corpo].adicionar_forca(Forca(None, vinculo.posicao, Vetor(0,1), self.indice_incognitas + 1))#1
                        else: #reação
                            lista_de_corpos[corpo].adicionar_forca(Forca(None, vinculo.posicao, Vetor(-1,0), self.indice_incognitas))#0
                            lista_de_corpos[corpo].adicionar_forca(Forca(None, vinculo.posicao, Vetor(0,-1), self.indice_incognitas + 1))#1
                    self.indice_incognitas += 2
                
                if (vinculo.tipo == "Apoio Simples"):
                    for corpo in vinculo.lista_corpos:
                        if(corpo == vinculo.lista_corpos[0]):
                            lista_de_corpos[corpo].adicionar_forca(Forca(None, vinculo.posicao, Vetor(0,1), self.indice_incognitas))#1
                        else: #reação
                            lista_de_corpos[corpo].adicionar_forca(Forca(None, vinculo.posicao, Vetor(0,-1), self.indice_incognitas))#0
                    self.indice_incognitas += 1
                
                if (vinculo.tipo == "Engaste"):
                    for corpo in vinculo.lista_corpos:
                        lista_de_corpos[corpo].adicionar_forca(Forca(None, vinculo.posicao, Vetor(1,0), self.indice_incognitas))
                        self.indice_incognitas += 1
                        lista_de_corpos[corpo].adicionar_forca(Forca(None, vinculo.posicao, Vetor(0,1), self.indice_incognitas))
                        self.indice_incognitas += 1
                        lista_de_corpos[corpo].adicionar_momento(Momento(None, self.indice_incognitas, 1))
                        self.indice_incognitas += 1
                    
                if (vinculo.tipo == "Conexao"): 
                    for corpo in vinculo.lista_corpos:
                        if(corpo == vinculo.lista_corpos[0]):
                            lista_de_corpos[corpo].adicionar_forca(Forca(None, vinculo.posicao, Vetor(1,0), self.indice_incognitas))
                            lista_de_corpos[corpo].adicionar_forca(Forca(None, vinculo.posicao, Vetor(0,1), self.indice_incognitas+1))
                            lista_de_corpos[corpo].adicionar_momento(Momento(None, self.indice_incognitas+2, 1))
                        else: #reação
                            lista_de_corpos[corpo].adicionar_forca(Forca(None, vinculo.posicao, Vetor(-1,0), self.indice_incognitas))
                            lista_de_corpos[corpo].adicionar_forca(Forca(None, vinculo.posicao, Vetor(0,-1), self.indice_incognitas+1))
                            lista_de_corpos[corpo].adicionar_momento(Momento(None, self.indice_incognitas+2, -1))
                    self.indice_incognitas += 3
        return lista_de_corpos
    
    def VetorVazioIncognitas(self):
        print("indice_incognitas:", self.indice_incognitas)
        VetorVazio = []
        for i in range(self.indice_incognitas):
            print("i vale:", i)
            VetorVazio.append(0)
        return VetorVazio