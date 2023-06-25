import numpy as np

class CarregamentosDistribuidos:
    def __init__ (self, tipoFuncao, coeficientes):
        self.tipoFuncao = tipoFuncao
        self.coeficientes = coeficientes #somente até o 2° grau, por enquanto
        