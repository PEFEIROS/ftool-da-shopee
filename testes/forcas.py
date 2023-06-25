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

# Resto do código de teste...

# Teste da classe Ponto
def teste_forca():
    
    # def __init__(self, vetor, ponto, versor=None, indice=None):
      
    # Teste da forca conhecida
    ponto_a = Ponto(5, 5)
    vetor_a = Vetor(4, 5)
    forca_a = Forca(vetor_a, ponto_a)

    print(forca_a.ponto.x, forca_a.ponto.y, forca_a.vetor.x, forca_a.vetor.y)
    
    # Teste da forca desconhecida
    versor_a = Vetor(1, 1)
    indice = 3
    forca_b = Forca(None,ponto_a,versor_a, indice)
    
    print(forca_b.ponto.x, forca_b.ponto.y, forca_b.versor.x, forca_b.versor.y, forca_b.indice)
# Chama a função de teste para a classe Ponto
teste_forca()
