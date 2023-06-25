import sys
import os

# Adicione o caminho do diretório "vetores" ao PYTHONPATH
diretorio_vetores = os.path.abspath(os.path.join(os.path.dirname(__file__), '../vetores'))
sys.path.append(diretorio_vetores)

from Ponto import Ponto

# Resto do código de teste...

# Teste da classe Ponto
def teste_ponto():
    # Teste do construtor
    a = Ponto(2, 3)
    b = Ponto(4, 6)

    # Teste do método get_coordenadas
    print(a.x , a.y)  # Saída: (2, 3)
    print(b.x , b.y)  # Saída: (4, 6)

# Chama a função de teste para a classe Ponto
teste_ponto()
