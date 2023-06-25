### por hora não usaremos
import sys
import os

# Adicione o caminho dos diretórios ao PYTHONPATH
diretorio_entidades = os.path.abspath(os.path.join(os.path.dirname(__file__), '../entidades'))
sys.path.append(diretorio_entidades)
diretorio_vetores = os.path.abspath(os.path.join(os.path.dirname(__file__), '../vetores'))
sys.path.append(diretorio_vetores)
diretorio_corpos = os.path.abspath(os.path.join(os.path.dirname(__file__), '../corpos'))
sys.path.append(diretorio_corpos)
diretorio_resolutor = os.path.abspath(os.path.join(os.path.dirname(__file__), '../resolutor'))
sys.path.append(diretorio_resolutor)

from CorpoRigido import CorpoRigido
from Forca import Forca
from Ponto import Ponto
from Vetor import Vetor
from Resolutor import Resolutor
from Momento import Momento

#Esta classe serve para listar todas as forcas, corpos, momentos e vinculos dados pelo usuario ao sistema

#receberemos:
#corpos:
#tipo, forcas, momentos -> todos conhecidos
#forcas conhecidas:
#ponto, vetor
#momentos conhecidos:
#momento

#vinculos -> que servem para entregar incognitas:
#tipo, ponto (posicao) -> os esforcos correspondentes serao dados pela gente.

class ListagemInicial:
#recebe uma lista muito louca de coisas do front end, inicializa tudo e coloca em sua respectiva lista.  
    def __init__(self):
        self.lista_forcas = []
        self.lista_corpos = []
        self.lista_momentos = []
        self.lista_vinculos = []
        self.lista_de_incognitas = []