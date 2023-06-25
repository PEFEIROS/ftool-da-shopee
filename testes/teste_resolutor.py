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


def teste_resolutor():

    #Pontos de interesse
    ponto_a = Ponto(0, 0)
    ponto_b = Ponto(1, 0)
    ponto_c = Ponto(2, 0)
    # Criar corpos
    corpo_a = CorpoRigido("BARRA")
    # Criar versores
    v_1 = Vetor(1,0)
    v_2 = Vetor(0,1)
    #Forca conhecida
    forca_1 = Forca(Vetor(0, -5), ponto_b)
    # Criar forças desconhecidas
    forca_ha = Forca(None, ponto_a, v_1, 0)
    forca_va = Forca(None, ponto_a, v_2, 1)
    forca_vc = Forca(None, ponto_c, v_2, 2)
    # Adicionar forças aos corpos
    corpo_a.adicionar_forca(forca_va)
    corpo_a.adicionar_forca(forca_ha)
    corpo_a.adicionar_forca(forca_1)
    corpo_a.adicionar_forca(forca_vc)
    
    #Calcula o momento
    momento_conhecido1 = Momento.calcular_momento(forca_1, ponto_a)

    #define o vetor de incognitas de acordo com o indice de cada incognita
    vetor_de_incognitas = [forca_ha, forca_va, forca_vc]

    # Criar lista de corpos
    lista_de_corpos = [corpo_a]

    # Criar resolutor
    resolutor = Resolutor(lista_de_corpos, vetor_de_incognitas)

    # Resolver o sistema
    resolutor.resolver()

    # Imprimir o vetor de incógnitas após a resolução
    print("resolução = ", resolutor.vetor_de_incognitas)


    print("\n\nteste2")
    #teste 2 - exercicio 1 da lista
    #Pontos de interesse
    ponto_a2 = Ponto(5, 7)
    ponto_c2 = Ponto(10, 7)

    # Criar versores
    v_1 = Vetor(1,0)
    v_2 = Vetor(0,1)

    #Forca conhecida
    forca_12 = Forca(Vetor(0, -7), ponto_c2)

    # Criar corpos
    corpo_a2 = CorpoRigido("BARRA")

    # Criar forças desconhecidas
    forca_va = Forca(None, ponto_a2, v_2, 2)
    forca_ha = Forca(None, ponto_a2, v_1, 1)

    # Adicionar forças aos corpos
    corpo_a2.adicionar_forca(forca_12)
    corpo_a2.adicionar_forca(forca_va)
    corpo_a2.adicionar_forca(forca_ha)

    # Criar momentos desconhecidos
    momen_p = Momento(None, 0, 1)

    #adiciona momentos aos corpos
    corpo_a2.adicionar_momento(momen_p)

    vetor_de_incognitas = [momen_p, forca_ha, forca_va]
    print("lista e: ", corpo_a2.lista_momentos[0].sentido)
    # Criar lista de corpos
    lista_de_corpos = [corpo_a2]

    # Criar resolutor
    resolutor2 = Resolutor(lista_de_corpos, vetor_de_incognitas)

    # Imprimir o vetor de incógnitas após a resolução
    
    # Resolver o sistema
    resolutor2.resolver()

    # Imprimir o vetor de incógnitas após a resolução
    print("resolução = ", resolutor2.vetor_de_incognitas)

teste_resolutor()