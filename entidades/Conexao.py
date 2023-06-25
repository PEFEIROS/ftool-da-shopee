from corpos.CorpoRigido import CorpoRigido

class Conexao (CorpoRigido):
    def __init__(self, tipo, x, y, angulo, corposAVincular):
        self.CorposVinculados = corposAVincular
        super().__init__(self, tipo, x, y, angulo)

   # def vincular (CorposVinculados, corposAVincular):
    #    for corpo in corposAVincular:
     #       if corpo not in CorposVinculados:
      #          CorposVinculados.append(corpo)
            
