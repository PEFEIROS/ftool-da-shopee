class Forca():
    #def __init__(self, vetor, ponto):
    #    """ construtor para força conhecida """
    #    self.vetor = vetor
    #    self.ponto = ponto
    #    self.conhecida = True
    
    #def __init__(self, versor, ponto, indice):
     #   """ construtor para força desconhecida """
     #   self.versor = versor
     #   self.ponto = ponto
     #   self.conhecida = False
     #   self.indice = indice # índice em relação ao vetor de incógnitas
        
    def __init__(self, vetor, ponto, versor=None, indice=None): #forca conhecida: forca = Forca(vetor, ponto)
        self.ponto = ponto                                      #forca desconhecida: forca = Forca(None, ponto, versor, indice)
        self.incognita = False if vetor is not None else True                                   
        
        if self.incognita:
            self.versor = versor
            self.indice = indice  
        else:
            self.vetor = vetor
