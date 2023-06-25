from corpos.CorpoRigido import CorpoRigido

class BarraDelgada (CorpoRigido):
    def __init__(self, tipo, x, y, angulo, comprimento):
        super().__init__(self, tipo, x, y, angulo)
        self.comprimento = comprimento
        
