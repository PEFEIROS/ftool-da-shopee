from corpos.CorpoRigido import CorpoRigido
from entidades.Referencial import Referencial

class ApoioSimples(CorpoRigido):
    def __init__(self, tipo, x, y, angulo):
        super().__init__(self, tipo, x, y, angulo)

    def local(self):
        # Implemente o comportamento específico da subclasse ApoioSimples
        # Utilize self.posicao conforme necessário
        pass

# Exemplo de criação de um objeto ApoioSimples
