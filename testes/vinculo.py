import sys
import os

# Adicione o caminho dos diretórios ao PYTHONPAHT
sys.path.append("/home/bertan/Documents/frontend-main/vetores")
diretorio_vinculos = os.path.abspath(os.path.join(os.path.dirname(__file__), '/home/bertan/Documents/frontend-main/corpos'))
sys.path.append(diretorio_vinculos)
diretorio_Forca = os.path.abspath(os.path.join(os.path.dirname(__file__), '/home/bertan/Documents/frontend-main/entidades'))
sys.path.append(diretorio_Forca)
diretorio_Corpo = os.path.abspath(os.path.join(os.path.dirname(__file__), '/home/bertan/Documents/frontend-main/corpos'))
sys.path.append(diretorio_Corpo)
diretorio_resolutor = os.path.abspath(os.path.join(os.path.dirname(__file__), '/home/bertan/Documents/frontend-main/resolutor'))
sys.path.append(diretorio_resolutor)

from Ponto import Ponto
from Vinculo import Vinculo
from CorpoRigido import CorpoRigido
from Forca import Forca
from Vetor import Vetor
from Momento import Momento
from Resolutor import Resolutor
from Montador_de_incognitas import MontadorDeIncognitas

#teste do inicializador do vinculo.
#o vinculo pode, essencialmente, ser apoio simples, duplo, engaste ou conexao.
#a conexao tem dois corpos associados, isso eh extremamente importante.

#Criacao de pontos e vinculos
#def __init__(self, tipo, posicao, corpo_1 = None, corpo_2 = None):
ponto_a = Ponto(0,0)
ponto_b = Ponto(0,5)
ponto_c = Ponto(5,5)
#ponto_d = Ponto(5,10)

vinculo_a = Vinculo("Apoio Duplo", ponto_a)
vinculo_b = Vinculo("Conexao", ponto_b)
vinculo_c = Vinculo("Apoio Simples", ponto_c)
#vinculo_c2 = Vinculo("Conexao", ponto_c)
#vinculo_d = Vinculo("Engaste", ponto_d)

#printar o conteúdo dos vinculos criados
print("teste 1: criacao de vinculos")

print("vinculo_a: ", vinculo_a.tipo, vinculo_a.posicao.x, vinculo_a.posicao.y)
print("vinculo_b: ", vinculo_b.tipo, vinculo_b.posicao.x, vinculo_b.posicao.y)
print("vinculo_c: ", vinculo_c.tipo, vinculo_c.posicao.x, vinculo_c.posicao.y)
#print("vinculo_c2: ", vinculo_c2.tipo, vinculo_c2.posicao.x, vinculo_c2.posicao.y)
#print("vinculo_d: ", vinculo_d.tipo, vinculo_d.posicao.x, vinculo_d.posicao.y)


#teste 2: criar corpos para colocar vinculos neles

vetor_a = Vetor(3,0)
vetor_b = Vetor(0,2)
vetor_c = Vetor(0,-4)
#vetor_d = Vetor(5,0)
ponto_a1 = Ponto(0,3)
ponto_b1 = Ponto(2,5)
ponto_c1 = Ponto(4,5)
#ponto_d1 = Ponto(5,7)

forca_a = Forca(vetor_a, ponto_a1)
forca_b = Forca(vetor_b, ponto_b1)
forca_c = Forca(vetor_c, ponto_c1)
#forca_d = Forca(vetor_d, ponto_d1)

corpo_a = CorpoRigido("a1")
corpo_b = CorpoRigido("b1")
#corpo_c = CorpoRigido("c1")

corpo_a.adicionar_forca(forca_a)
corpo_b.adicionar_forca(forca_b)
corpo_b.adicionar_forca(forca_c)
#corpo_c.adicionar_forca(forca_d)


#note que a conexao n eh um vinculo que deve ser adicionado aqui.
#nada impede, mas n ha a necessidade
#corpo_a.adicionar_vinculos(vinculo_a)
#corpo_b.adicionar_vinculos(vinculo_c)
#corpo_c.adicionar_vinculos(vinculo_d)

#adiciona os corpos que sofre a ação de cada vinculo na lista_corpos
vinculo_a.adiciona_corpo(0) #adiciona o indice do corpo_a

vinculo_b.adiciona_corpo(0)
vinculo_b.adiciona_corpo(1)

vinculo_c.adiciona_corpo(1)
#vinculo_c.adiciona_corpo(2)


lista_de_corpos1 = [corpo_a, corpo_b]
lista_de_vinculos = [vinculo_a, vinculo_b, vinculo_c]
#montador de incognitas.
montador1 = MontadorDeIncognitas()
lista_de_corpos2 = montador1.IncognitasCompleto(lista_de_corpos1, lista_de_vinculos)

#resolutor de equacoes.
vetor_incognita = montador1.VetorVazioIncognitas()

resolutor1 = Resolutor(lista_de_corpos2, vetor_incognita)

resolutor1.resolver()

print(resolutor1.vetor_de_incognitas)




#passo a passo:
# definir os pontos
#EX: ponto_a = Ponto(0, 0)

#definir os corpos, definindo o INDICE (inteiro positivo) 
#EX: corpo_c3 = CorpoRigido(0)

#definir os vinculos do sistema com o NOME DO VINCULO e o ponto onde ele está
#EX: vinculo1 = Vinculo("Apoio Simples", ponto_c)
#Obs: Apenas tipos bem específicos devem ser passados como argumentos e da forma correta.
#"Apoio Simples", "Apoio Duplo", "Engaste" e "Conexao"

#vincular os corpos em cada vinculo
#EX: vinculo1.adiciona_corpo(0) 
#OBS: O NUMERO DO ARGUMENTO (NESSE CASO 0) É O INDICE DO CORPO NA LISTA DE CORPOS

#Definir as forças 
#EX: forca_1 = Forca(Vetor(0,-400), ponto_b)

#Adicionar as forças que atuam em cada corpo
#EX: corpo_c3.adicionar_forca(forca_1)

#Definir os momentos conhecidos
#EX: momento_conhecido2 = Momento(300)

#Adicionar os momentos conhecidos onde "está sendo aplicado o momento"
#EX: corpo_c3.adicionar_momento(momento_conhecido2)

#definir a lista de vinculos existentes
#EX: lista_de_vinculos = [vinculo1, vinculo2]

#definir a lista de corpos existentes (somente barras)
#EX: lista_de_corpos3 = [corpo_c3]

#Criar o montador de incognitas
#montador2 = MontadorDeIncognitas()

#Criar o vetor de incognitas
#Ex: vetor_de_incognitas = montador2.VetorVazioIncognitas

#Criar o Resolutor
#Ex: resolutor = Resolutor(lista de corpos, vetor de incognitas)

# Resolver o sistema
#resolutor2.resolver()

#Para printar a solução
#EX:
# print("solução e: ")
# print(resolutor2.vetor_de_incognitas)


#Pontos de interesse
ponto_a = Ponto(0, 0)
ponto_b = Ponto(200, 0)
ponto_c = Ponto(300, 0)
# Criar corpos
corpo_c3 = CorpoRigido(0)
vinculo1 = Vinculo("Apoio Simples", ponto_c)
vinculo2 = Vinculo("Apoio Duplo", ponto_a)

#coloca os corpos onde o vinculo atua
vinculo1.adiciona_corpo(0)
vinculo2.adiciona_corpo(0)
#Forca conhecida

forca_1 = Forca(Vetor(0,-400), ponto_b)

# Adicionar forças aos corpos
corpo_c3.adicionar_forca(forca_1)

#Calcula o momento

momento_conhecido2 = Momento(300)
# adicionar
corpo_c3.adicionar_momento(momento_conhecido2)
# Criar lista de corpos
lista_de_corpos3 = [corpo_c3]


# Criar o Montador de equações
montador2 = MontadorDeIncognitas()

# def IncognitasCompleto(self, lista_de_corpos3, lista_de_vinculos): 

#define a lista de vinculos
lista_de_vinculos = [vinculo1, vinculo2]

lista_de_corpos3 = montador2.IncognitasCompleto(lista_de_corpos3, lista_de_vinculos)

vetor_de_incognitas = montador2.VetorVazioIncognitas()

# Criar resolutor
resolutor2 = Resolutor(lista_de_corpos3, vetor_de_incognitas)

# Resolver o sistema
resolutor2.resolver()
print("solução e: ")
print(resolutor2.vetor_de_incognitas)


