import numpy as np
import sys
import os

# Adicione o caminho dos diretórios ao PYTHONPATH
diretorio_entidades = os.path.abspath(os.path.join(os.path.dirname(__file__), '../entidades'))
sys.path.append(diretorio_entidades)
diretorio_vetores = os.path.abspath(os.path.join(os.path.dirname(__file__), '../vetores'))
sys.path.append(diretorio_vetores)

from Momento import Momento
from Ponto import Ponto

class Resolutor:
    def __init__(self, lista_de_corpos, vetor_de_incognitas):
        self.lista_de_corpos = lista_de_corpos
        self.vetor_de_incognitas = vetor_de_incognitas


    def resolver(self):
        """" resolve as equações de equilíbrio """
        equacoes = []

        for corpo in self.lista_de_corpos:
            # impor equilíbrio para cada corpo
            equacoes.append(self.equilibrio_x(corpo))
            equacoes.append(self.equilibrio_y(corpo))
            equacoes.append(self.equilibrio_momentos(corpo))
        print("equacoes: ", equacoes)
        self.vetor_de_incognitas = self.resolver_sistema_linear(equacoes)
        

    def resolver_sistema_linear(self, equacoes):
        """ resolve o sistema linear """
        print("equações = ", equacoes)
        matriz_aumentada = np.array(equacoes)
        print("matriz aumentada: \n", matriz_aumentada)
        
        # matriz_coeficientes = matriz_aumentada[:, -2]
        #matriz_coeficientes = matriz_aumentada[:, -2]
        matriz_coeficientes = matriz_aumentada[:, :-1]
        print("matriz_coeficientes: \n", matriz_coeficientes)
        
        vetor_independente = matriz_aumentada[:, -1]
        print("vetor independente: \n", vetor_independente)

        solucao = np.linalg.solve(matriz_coeficientes, vetor_independente)
        return solucao
  
    def equilibrio_x(self, corpo):
        """" retornar equação de equilíbrio em x """
        equacao = self.equacao_vazia()

        # impor equilíbrio
        for forca in corpo.lista_forcas:
            # somar forcas em x
            if(forca.incognita == False):
                # força conhecida
                equacao[-1] = equacao[-1] - forca.vetor.x
            elif forca.incognita == True:
                #força desconhecida
                equacao[forca.indice] = equacao[forca.indice] + forca.versor.x
        print("x = ", equacao)
        return equacao

    def equilibrio_y(self, corpo):
        """" retornar equação de equilíbrio em y """
        equacao = self.equacao_vazia()

        # impor equilíbrio
        for forca in corpo.lista_forcas:
            # somar forcas em y
            if(forca.incognita == False):
                # força conhecida
                equacao[-1] = equacao[-1] - forca.vetor.y
            else:
                # força desconhecida
                equacao[forca.indice] = equacao[forca.indice] + forca.versor.y
        print("y = ", equacao)
        return equacao
    

    def equilibrio_momentos(self, corpo):
        """" retornar equação de equilíbrio de momentos """
        equacao = self.equacao_vazia()

        #impondo o equilibrio
        for momento in corpo.lista_momentos: 
            if (momento.incognita == False):
                # momento conhecida
                equacao[-1] = equacao[-1] - momento.momento
            else:
                #momento desconhecido 
                equacao[momento.indice] = equacao[momento.indice] + momento.sentido

        for forca in corpo.lista_forcas:
                if (forca.incognita == False):
                    #momento de força conhecida
                    equacao[-1] = equacao[-1] - Momento.calcular_momento(forca, Ponto(0,0)).momento

                else:
                    #momento de força desconhecida
                    equacao[forca.indice] += Momento.calcular_momento(forca, Ponto(0,0)) #calcula em relação a origem
        print("Momento = ", equacao)
        return equacao

    def equacao_vazia(self):
        """ cria um vetor de equação todo nulo """
        equacao = []

        # zera a equação
        for i in range (0, len(self.vetor_de_incognitas) + 1):
            equacao.append(0)

        return equacao
