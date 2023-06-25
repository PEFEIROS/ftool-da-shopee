class Vinculo:
    def __init__(self, tipo, posicao):
        self.tipo = tipo
        self.posicao = posicao
        self.lista_corpos = []
        
    def adiciona_corpo(self, corpo):
        self.lista_corpos.append(corpo)