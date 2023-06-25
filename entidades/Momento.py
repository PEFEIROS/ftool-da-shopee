import sys
import os

# Adicione o caminho dos diretórios ao PYTHONPATH
diretorio_entidades = os.path.abspath(os.path.join(os.path.dirname(__file__), '../entidades'))
sys.path.append(diretorio_entidades)

from Forca import Forca


class Momento:
    
    #inicializador:
    #conhecido: tem momento
    #desconhecido: tem indice e sentido

    def __init__(self, momento=None, indice=None, sentido=None): 
        self.incognita = False if momento is not None else True
        
        if (self.incognita):
            self.indice = indice #representa uma posicao no vetor de equacao
            self.sentido = sentido
        else:
            self.momento = momento
    
    def calcular_momento(forca, ponto):
        dist_x = forca.ponto.x - ponto.x
        dist_y = forca.ponto.y - ponto.y #v = (dist_x, dist_y)
        if forca.incognita == False:
        #caso a forca nao seja desconhecida
            #print("forca = (", forca.vetor.x, ",", forca.vetor.y, ")")
            #print("dist = (", dist_x, ",", dist_y, ")") Força = (0, -5)
            momento = dist_x * forca.vetor.y - (forca.vetor.x * dist_y)
            #print("momento = ", "(", forca.vetor.x, ",", forca.vetor.y, ", 0) ^ (", dist_x, ",", dist_y, ", 0) = (0, 0, ",momento, ")")
            return Momento(momento)
        #caso a forca seja desconhecida
        else:
            momento = - (forca.versor.x * dist_y) + dist_x * forca.versor.y
            return momento
        
                 
    def teste(self):
        if self.incognita:
            print("Momento desconhecido:")
            print("Índice:", self.indice)
            print("Sentido:", self.sentido)
        else:
            print("Momento conhecido:")
            print("Valor:", self.momento)
            
    #def __init__(self, momento):
    #    """" momento conhecido """
    #    self.momento = momento
    #    self.incognita = False
    
    #def __init__(self, indice, sentido):
    #    """" momento desconhecido """
    #    self.indice = indice # índice do momento no vetor de incógnitas
    #    self.sentido = sentido # sentido do momento desconhecido
    #    self.incognita = True

    #def momento(forca, ponto):
        # força = (x1,y1,0)
        # ponto = (x2,y2,0)
        # M = r^f = (0, 0, x1*y2 - x2*y1)
    #    return Momento(forca.x*ponto.y - ponto.x*forca.y)

