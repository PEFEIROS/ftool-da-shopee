import sys
import os

# Adicione o caminho dos diretórios ao PYTHONPATH
diretorio_vetores = os.path.abspath(os.path.join(os.path.dirname(__file__), '../vetores'))
sys.path.append(diretorio_vetores)

from Vetor import Vetor

def testeVetor():
    # Criando vetores para teste
    vetor1 = Vetor(2, 3)
    vetor2 = Vetor(4, 1)

    # Testando o método de soma estático
    vetor3 = Vetor.soma(vetor1, vetor2)
    print(vetor3.x, vetor3.y)  # Saída: 6 4

    # Testando o cálculo do módulo
    modulo_vetor1 = vetor1.modulo()
    print(modulo_vetor1)  # Saída: 3.605551275463989

    # Testando o cálculo do ângulo
    angulo_vetor1 = vetor1.angle()
    print(angulo_vetor1)  # Saída: 0,9827937232 rad

    # Testando a multiplicação escalar
    vetor1.multiplicacao_escalar(2)
    print(vetor1.x, vetor1.y)  # Saída: 4 6

    # Testando o produto escalar
    print("Vetor1 = (", vetor1.x, vetor1.y, ")")
    print("Vetor1 = (", vetor2.x, vetor2.y, ")")
    produto_escalar = Vetor.produto_escalar(vetor1, vetor2)
    print(produto_escalar)  # Saída: 11

    # Testando a normalização
    vetor1.normalizar()
    print(vetor1.x, vetor1.y)  # Saída: 0.5547001962252291 0.8320502943378437
testeVetor()