import numpy as np

class Vetor:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    

    def soma(vetor_a, vetor_b):
        """ soma dois vetores """
        novo_x = vetor_a.x + vetor_b.x
        novo_y = vetor_a.y + vetor_b.y
        return Vetor(novo_x, novo_y)
    

    def modulo(self):
        return np.sqrt((self.x*self.x) + (self.y*self.y))


    def angle(self):
        return np.arctan2(self.y, self.x)


    def multiplicacao_escalar(self, escalar):
        self.x = self.x*escalar
        self.y = self.y*escalar
    

    def normalizar(self):
        self.multiplicacao_escalar(1/self.modulo())


    def produto_escalar(vetor_a, vetor_b):
        """ realiza o produto escalar de dois vetores"""
        (produto_escalar) = (vetor_a.x*vetor_b.x) + (vetor_a.y*vetor_b.y)
        return produto_escalar 