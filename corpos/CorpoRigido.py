class CorpoRigido:
    def __init__(self, nome):
        self.nome = nome
        self.lista_forcas = [] 
        self.lista_momentos = []
        self.lista_vinculos = []
    
    def adicionar_forca(self, forca):
        self.lista_forcas.append(forca)
   
    def adicionar_momento(self, momento):
        self.lista_momentos.append(momento)
        
    def adicionar_vinculos(self, vinculo):
        self.lista_vinculos.append(vinculo)









