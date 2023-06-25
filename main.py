from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import Image,ImageTk
import math
import numpy as np

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

def main():
    global botaoNum
    global botaoCoord
    botaoNum = 0
    root = tk.Tk()
    global imgEngaste
    global imgArticulacao
    global imgApoioSimples
    global imgJuncao
    global imgMomento

    imgEngaste =  ImageTk.PhotoImage(Image.open("./ENGASTE.png"))
    imgArticulacao =  ImageTk.PhotoImage(Image.open("./ARTICULACAO.png"))
    imgApoioSimples =  ImageTk.PhotoImage(Image.open("./APOIOSIMPLES.png"))
    imgJuncao =  ImageTk.PhotoImage(Image.open("./JUNCAO.png"))
    imgMomento =  ImageTk.PhotoImage(Image.open("./MOMENTO.png"))
    
    root.title('FTool da Shopee')
    root.geometry('800x640')
    ico = Image.open('Frame-8.ico')
    photo = ImageTk.PhotoImage(ico)
    root.wm_iconphoto(False, photo)
    # dicionario das coordenadas das barras
    coords = {"x":0,"y":0,"x2":0,"y2":0}
    botaoCoord = {"relx":0.01, "rely":0.25}
    # lista que armazena todas as coordenadas das barras
    lines = []
    text = []
    botaoBarra = []
    vinculos = [[[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], 
                [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], 
                [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], 
                [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], 
                [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], 
                [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], 
                [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], 
                [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], 
                [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], 
                [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], 
                [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]]]
    
    momentos = [[[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], 
                [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], 
                [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], 
                [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], 
                [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], 
                [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], 
                [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], 
                [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], 
                [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], 
                [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], 
                [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]]]

    
    # label 1
    label1 = tk.Label(root, bg='#abaaa9')
    label1.place(relx=0, rely=0.5, relwidth=0.2, relheight=1, anchor='w')

    canvas = Canvas(root, bg="#ffffff")
    canvas.place(relx=1, rely=0.5, relwidth=0.8, relheight=1, anchor='e')
    
    forcas = [{"f1":canvas.create_line(0, 0, 0, 0, arrow=tk.LAST, width=2), 
               "f2":canvas.create_line(0, 0, 0, 0, arrow=tk.LAST, width=2), 
               "f3":canvas.create_line(0, 0, 0, 0, arrow=tk.LAST, width=2)}]
    
    for i in range(100):
        forcas.append({"f1":canvas.create_line(0, 0, 0, 0, arrow=tk.LAST, width=2), 
                       "f2":canvas.create_line(0, 0, 0, 0, arrow=tk.LAST, width=2), 
                       "f3":canvas.create_line(0, 0, 0, 0, arrow=tk.LAST, width=2)})
    
    text.append(canvas.create_text(50, 50, text="x1: ", fill="black", font='Calibri 12'))
    text.append(canvas.create_text(50, 80, text="y1: ", fill="black", font='Calibri 12'))
    text.append(canvas.create_text(130, 50, text="x2: ", fill="black", font='Calibri 12'))
    text.append(canvas.create_text(130, 80, text="y2: ", fill="black", font='Calibri 12'))

    barra = tk.Button(root, text='Adicionar barras', command=lambda: adicionaBarra(barra, coords, canvas, 
                                                                                   lines, text, botaoBarra, 
                                                                                   root, forcas, vinculos, momentos))
    
    calcula = tk.Button(root, text='Calcular', command=lambda: showInfo(lines, forcas, botaoBarra, 
                                                                        vinculos, momentos, root, canvas))
    calcula.place(relx=0.02, rely=0.90, relwidth=0.15, relheight=0.04, anchor='w')

    barra.place(relx=0.02, rely=0.05, relwidth=0.15, relheight=0.04, anchor='w')
        
    root.mainloop()


def showInfo(lines, forcas, botaoBarra, vinculos, momentos, root, canvas):
    info = Toplevel(root)
    info.title("Resultados")
    info.geometry('480x480')
    info.minsize(400, 400)
    info.maxsize(400, 400)
    indiceBarras = []
    infoForcas = [[{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}], [{}]]
    infoVinculos = [[]]
    infoMomentos = [[]]
    
    for i in range(100):
        try:
            if lines[i] != None:
                indiceBarras.append(i)
        except:
            pass
    
    print(canvas.coords(forcas[i]["f1"])[0])
    for i in range(100):
        try:
            if (canvas.coords(forcas[i]["f1"])[0] != 0 or
                canvas.coords(forcas[i]["f2"])[0] != 0 or
                canvas.coords(forcas[i]["f3"])[0] != 0):

                    modulo = anguloForca(canvas, forcas[i]["f1"])[0]
                    angulo = anguloForca(canvas, forcas[i]["f1"])[1]
                    aux = [canvas.coords(forcas[i]["f1"])[0],
                           canvas.coords(forcas[i]["f1"])[3],
                           round(-math.cos(np.deg2rad(angulo))*modulo),
                           round(-math.sin(np.deg2rad(angulo))*modulo)]
                    infoForcas[i].append({"index":i})
                    infoForcas[i].append({"1":aux})

                    modulo = anguloForca(canvas, forcas[i]["f2"])[0]
                    angulo = anguloForca(canvas, forcas[i]["f2"])[1]
                    aux = [canvas.coords(forcas[i]["f2"])[0],
                           canvas.coords(forcas[i]["f2"])[3],
                           round(-math.cos(np.deg2rad(angulo))*modulo),
                           round(-math.sin(np.deg2rad(angulo))*modulo)]
                    infoForcas[i].append({"2":aux})

                    modulo = anguloForca(canvas, forcas[i]["f3"])[0]
                    angulo = anguloForca(canvas, forcas[i]["f3"])[1]
                    aux = [canvas.coords(forcas[i]["f3"])[0],
                           canvas.coords(forcas[i]["f3"])[3],
                           round(-math.cos(np.deg2rad(angulo))*modulo),
                           round(-math.sin(np.deg2rad(angulo))*modulo)]
                    infoForcas[i].append({"3":aux})
        except:
            pass
        
    for i in range(100):
        for j in range(100):
            if vinculos[i] != [[]]:
                try:
                    infoVinculos.append(vinculos[i][j])
                except:
                    pass

    for i in range(100):
        for j in range(100):
            try:
                if momentos[i] != [[]]:
                    infoMomentos.append(momentos[i][j])
            except:
                pass

    # MANDAR PARA BACKEND

    # # Criar corpos
    # corpo_c3 = CorpoRigido(0)
    corpos = []
    for barra in indiceBarras:
        corpos.append(CorpoRigido(barra))

    # #coloca os corpos onde o vinculo atua
    # vinculo1.adiciona_corpo(0)
    # vinculo2.adiciona_corpo(0)
    vinculosResolutor = []
    i = 0
    print(vinculos)
    for vinculoArray in vinculos:
        for vinculo in vinculoArray:
            if vinculo != []:
                vinculoCreated = Vinculo(str(vinculo[1]), Ponto(vinculo[0][0], vinculo[0][1]))
                vinculoCreated.adiciona_corpo(indiceBarras[i])
                vinculosResolutor.append(vinculoCreated)
        i += 1

    forcas = []
    for forcaArray in infoForcas:
        i = 2
        if len(forcaArray) > 1:
            if forcaArray[2]['1'][0] != 0 or forcaArray[2]['1'][1] != 0: 
                forcinha = Forca(Vetor(forcaArray[2]['1'][2],
                                       forcaArray[2]['1'][3]),
                                       Ponto(forcaArray[2]['1'][0],
                                             forcaArray[2]['1'][1]))
                forcas.append(forcinha)
                corpos[0].adicionar_forca(forcinha)
            
            if forcaArray[3]['2'][0] != 0 or forcaArray[3]['2'][1] != 0: 
                forcinha = Forca(Vetor(forcaArray[3]['2'][2],
                                       forcaArray[3]['2'][3]),
                                       Ponto(forcaArray[3]['2'][0],
                                             forcaArray[3]['2'][1]))
                forcas.append(forcinha)
                corpos[0].adicionar_forca(forcinha)
            if forcaArray[4]['3'][0] != 0 or forcaArray[4]['3'][1] != 0: 
                forcinha = Forca(Vetor(forcaArray[4]['3'][2],
                                       forcaArray[4]['3'][3]),
                                       Ponto(forcaArray[4]['3'][0],
                                             forcaArray[4]['3'][1]))
                forcas.append(forcinha)
                corpos[0].adicionar_forca(forcinha)

    # #Calcula o momento

    # momento_conhecido2 = Momento(300)
    # # adicionar
    # corpo_c3.adicionar_momento(momento_conhecido2)
    momentos = []
    for momento in infoMomentos:
        if momento != []:
            momentinho = Momento(int(momento[2]))
            momentos.append(momentinho)
            corpos[0].adicionar_momento(momentinho)

    try:
        # Criar o Montador de equações
        montador2 = MontadorDeIncognitas()
        
        lista_de_corpos3 = montador2.IncognitasCompleto([corpos[0]], vinculosResolutor)

        vetor_de_incognitas = montador2.VetorVazioIncognitas()

        # Criar resolutor
        resolutor2 = Resolutor(lista_de_corpos3, vetor_de_incognitas)

        # Resolver o sistema
        resolutor2.resolver()
        print("solução e: ")
        resolucao = resolutor2.vetor_de_incognitas
    except:
        messagebox.showwarning("Atenção", "O sistema não é isostático!")

    text = Text(info, width=80, height=80, background='#abaaa9')
    j = 0
    for vinculo in infoVinculos:
        if vinculo != []:
            if vinculo[1] == "Apoio Simples":
                text.insert('1.0', "Fy: {}\n".format(round(resolucao[j], 2)))
                text.insert('1.0', "Apoio Simples\n")
                j += 1
            elif vinculo[1] == "Apoio Duplo":
                text.insert('1.0', "Fy: {}\n".format(round(resolucao[j+1], 2)))
                text.insert('1.0', "Fx: {}\n".format(round(resolucao[j], 2)))
                text.insert('1.0', "Apoio Duplo\n")
                j += 2
        
            elif vinculo[1] == "Juncao":
                text.insert('1.0', "Momento: {}\n".format(round(resolucao[j+2], 2)))
                text.insert('1.0', "Fy: {}\n".format(round(resolucao[j+1], 2)))
                text.insert('1.0', "Fx: {}\n".format(round(resolucao[j], 2)))
                text.insert('1.0', "Juncao\n")
                j += 3
            else:
                text.insert('1.0', "Momento: {}\n".format(round(resolucao[j+2], 2)))
                text.insert('1.0', "Fy: {}\n".format(round(resolucao[j+1], 2)))
                text.insert('1.0', "Fx: {}\n".format(round(resolucao[j], 2)))
                text.insert('1.0', "Engaste\n")
                j += 3

    text.pack(expand=True)
    text["state"] = "disabled"


def adicionarEngaste(x, y, canvas):
    global imgEngaste
    img = canvas.create_image(x,y,anchor=N,image=imgEngaste)
    return img


def adicionarArticulacao(x, y, canvas):
    global imgArticulacao
    img = canvas.create_image(x,y,anchor=N,image=imgArticulacao) 
    return img

def adicionarApoioSimples(x, y, canvas):
    global imgApoioSimples
    img = canvas.create_image(x,y,anchor=N,image=imgApoioSimples)
    return img

def adicionarJuncao(x, y, canvas):
    global imgJuncao
    img = canvas.create_image(x,y,anchor=CENTER,image=imgJuncao)
    return img

def adicionarMomento(x, y, canvas):
    global imgMomento
    img = canvas.create_image(x,y,anchor=CENTER,image=imgMomento)
    return img
    
    
def adicionaBarra(barra, coords, canvas, lines, text, botaoBarra, root, forcas, vinculos, momentos):
    barra.config(relief=SUNKEN)
    canvas.bind("<ButtonPress-1>", lambda event: click(coords, canvas, lines, botaoBarra, 
                                                       root, barra, forcas, vinculos, momentos,
                                                       e=event))
    canvas.bind("<B1-Motion>", lambda event: drag(coords, canvas, lines, text, e=event))

    
def click(coords, canvas, lines, botaoBarra, 
          root, barra, forcas, vinculos, momentos, e):
    # define start point for line
    coords["x"] = e.x
    coords["y"] = e.y
    # create a line on this point and store it in the list
    for line in lines:
        if type(line) != type(None):
            coordenadas = canvas.coords(line)
            if abs(canvas.coords(line)[0] - coords["x"]) < 12 and abs(canvas.coords(line)[1] - coords["y"]) < 12:
                coords["x"] = canvas.coords(line)[0]
                coords["y"] = canvas.coords(line)[1]
    
    lines.append(canvas.create_line(coords["x"], coords["y"], coords["x"], coords["y"], fill="black", width=4))

    adicionaBarraBotao(botaoBarra, root, barra, canvas, lines, forcas, vinculos, momentos)
    
    
def adicionaBarraBotao(botaoBarra, root, barra, canvas, lines, forcas, vinculos, momentos): 
    global botaoNum
    global botaoCoord
    botaoBarra.append(tk.Button(root, text="Barra {}".format(botaoNum + 1), 
                                command=lambda num=botaoNum: botaoMenu(num, root, barra, canvas, 
                                                                       lines, forcas, botaoBarra, vinculos, momentos)))
    botaoBarra[-1].place(relx=botaoCoord["relx"], rely=botaoCoord["rely"], relwidth=0.05, relheight=0.04, anchor='w')
    botaoNum += 1
    botaoCoord["relx"] += 0.06
    
    if (botaoCoord["relx"] > 0.14):
        botaoCoord["relx"] = 0.01
        botaoCoord["rely"] += 0.06


def drag(coords, canvas, lines, text, e):
    # update the coordinates from the event
    coords["x2"] = e.x
    coords["y2"] = e.y

    # Change the coordinates of the last created line to the new coordinates    
    difX = abs(coords["x"] - coords["x2"])
    difY = abs(coords["y"] - coords["y2"])
    if difY < 20:
        coords["y2"] = coords["y"]
    if difX < 20:
        coords["x2"] = coords["x"]
    
    for line in lines:
        if type(line) != type(None):
            coordenadas = canvas.coords(line)
            if abs(canvas.coords(line)[0] - coords["x"]) < 12 and abs(canvas.coords(line)[1] - coords["y"]) < 12:
                coords["x"] = canvas.coords(line)[0]
                coords["y"] = canvas.coords(line)[1]

            if abs(canvas.coords(line)[2] - coords["x2"]) < 12 and abs(canvas.coords(line)[3] - coords["y2"]) < 12:
                coords["x2"] = canvas.coords(line)[2]
                coords["y2"] = canvas.coords(line)[3]
    
    canvas.itemconfigure(text[0], text="x1: {}".format(coords["x"]))
    canvas.itemconfigure(text[1], text="y1: {}".format(coords["y"]))
    canvas.itemconfigure(text[2], text="x2: {}".format(coords["x2"]))
    canvas.itemconfigure(text[3], text="y2: {}".format(coords["y2"]))
    
    canvas.coords(lines[-1], coords["x"], coords["y"], coords["x2"], coords["y2"])   
   
    
def botaoMenu(num, root, barra, canvas, lines, forcas, botaoBarra, vinculos, momentos):
    barra.config(relief=RAISED)
    canvas.unbind("<ButtonPress-1>")
    canvas.unbind("<B1-Motion>")
    canvas.itemconfigure(lines[num], fill="blue")
    
    janela = Toplevel(root)
    janela.title("Barra {}".format(num + 1))
    janela.geometry('480x360')
    janela.minsize(390, 280)
    janela.maxsize(480, 360)
    
    # x label
    xVar = tk.StringVar()
    xLabel = tk.Label(janela, text='Coordenada x1')
    xLabel.grid(row=0, column=0, padx=5)
    
    # x entry
    xEntry = tk.Entry(janela, textvariable=xVar, borderwidth=5, width=10, relief=tk.FLAT)
    xEntry.insert(0, canvas.coords(lines[num])[0])
    xEntry.grid(row=1, column=0, padx=5, pady=5)
    
    # y label
    yVar = tk.StringVar()
    yLabel = tk.Label(janela, text='Coordenada y1')
    yLabel.grid(row=0, column=1, padx=5)
    
    #y entry
    yEntry = tk.Entry(janela, textvariable=yVar, borderwidth=5, width=10, relief=tk.FLAT)
    yEntry.insert(0, canvas.coords(lines[num])[1])
    yEntry.grid(row=1, column=1, padx=5, pady=5)
    
    # x2 label
    x2Var = tk.StringVar()
    x2Label = tk.Label(janela, text='Coordenada x2')
    x2Label.grid(row=2, column=0, padx=5)
    
    # x2 entry
    x2Entry = tk.Entry(janela, textvariable=x2Var, borderwidth=5, width=10, relief=tk.FLAT)
    x2Entry.insert(0, canvas.coords(lines[num])[2])
    x2Entry.grid(row=3, column=0, padx=5, pady=5)
    
    # y2 label
    y2Var = tk.StringVar()
    y2Label = tk.Label(janela, text='Coordenada y2')
    y2Label.grid(row=2, column=1, padx=5)

    # y2 entry
    y2Entry = tk.Entry(janela, textvariable=y2Var, borderwidth=5, width=10, relief=tk.FLAT)
    y2Entry.insert(0, canvas.coords(lines[num])[3])
    y2Entry.grid(row=3, column=1, padx=5, pady=5)
    
    mt = moduloTan(num, canvas, lines)
    modulo = mt[0]
    tan = mt[1]
    
    # r label
    rVar = tk.StringVar()
    rLabel = tk.Label(janela, text='r')
    rLabel.grid(row=0, column=2, padx=5)
    
    # r entry
    rEntry = tk.Entry(janela, textvariable=rVar, borderwidth=5, width=10, relief=tk.FLAT)
    rEntry.insert(0, "{:.2f}".format(modulo))
    rEntry.grid(row=1, column=2, padx=5, pady=5)

    # theta label
    thetaVar = tk.StringVar()
    thetaLabel = tk.Label(janela, text='θ')
    thetaLabel.grid(row=2, column=2, padx=5)

    # theta entry
    thetaEntry = tk.Entry(janela, textvariable=thetaVar, borderwidth=5, width=10, relief=tk.FLAT)
    thetaEntry.insert(0, "{:.2f}".format(tan))
    thetaEntry.grid(row=3, column=2, padx=5, pady=5)
    
    # aplicar coordenadas button
    aplicarCoord = tk.Button(janela, text="Mudar coordenadas", 
                             command=lambda: mudarCoords(num, xVar, yVar, x2Var, 
                                                         y2Var, rVar, thetaVar, canvas, 
                                                         lines, rEntry, thetaEntry, forcas, vinculos))
    aplicarCoord.grid(row=4, column=0, padx=5, pady=5, sticky=tk.N, columnspan=2)
    
    # aplicar polares button
    aplicarPol = tk.Button(janela, text="Mudar Polares", 
                           command=lambda: mudarPol(num, xVar, yVar, x2Var, 
                                                    y2Var, rVar, thetaVar, canvas, 
                                                    lines, xEntry, yEntry, x2Entry, 
                                                    y2Entry, forcas, vinculos))
    aplicarPol.grid(row=4, column=2, padx=5, pady=5, sticky=tk.W)
    
    spacer1 = tk.Label(janela, text=" ",)
    spacer1.grid(row=5, column=0)
    
    # adicionar forca button
    adicionarForca1 = tk.Button(janela, text="Força concentrada 1", 
                                command=lambda: addForca(num, mt[1], canvas, lines, 
                                                         forcas[num]["f1"], janela))
    adicionarForca1.grid(row=6, column=0, padx=5, pady=5, sticky=tk.N)
    
    adicionarForca2 = tk.Button(janela, text="Força concentrada 2", 
                                command=lambda: addForca(num, mt[1], canvas, lines, 
                                                         forcas[num]["f2"], janela))
    adicionarForca2.grid(row=6, column=1, padx=5, pady=5, sticky=tk.N)
    
    adicionarForca3 = tk.Button(janela, text="Força concentrada 3", 
                                command=lambda: addForca(num, mt[1], canvas, lines, 
                                                         forcas[num]["f3"], janela))
    adicionarForca3.grid(row=6, column=2, padx=5, pady=5, sticky=tk.N)
    
    spacer2 = tk.Label(janela, text="")
    spacer2.grid(row=7, column=0, columnspan=3)
    
    # adicionar vínculo
    addVinculos = tk.Button(janela, text="Adicionar vínculo", 
                        command=lambda: addVinculo(num, mt[1], canvas, lines, vinculos, janela))
    addVinculos.grid(row=8, column=0, padx=5, pady=5, sticky=tk.W)

    addMomentos = tk.Button(janela, text="Adicionar momento", 
                        command=lambda: addMomento(num, mt[1], canvas, lines, momentos, janela))
    addMomentos.grid(row=8, column=1, padx=5, pady=5, sticky=tk.W) 

    # excluir button
    excluir = tk.Button(janela, text="Excluir Barra", 
                        command=lambda: excluirBarra(num, janela, canvas, 
                                                     botaoBarra, lines, forcas, vinculos))

    excluir.grid(row=8, column=2, padx=5, pady=5, sticky=tk.W) 
    
    janela.protocol("WM_DELETE_WINDOW", lambda arg=canvas, arg1=lines, arg2=num, 
                    arg3=janela: mudaCor(arg, arg1, arg2, arg3))
    

def mudaCor(canvas, lines, num, janela):
    canvas.itemconfigure(lines[num], fill="black")
    janela.destroy()
    
    
def addMomento(num, theta, canvas, lines, momentos, janela):
    janela = Toplevel(janela)
    janela.title("Adicionar momentos {}".format(num + 1))
    janela.geometry('680x240')
    janela.minsize(340, 120)
    janela.maxsize(480, 240)

    # forca label
    momentoVar = tk.StringVar()
    momentoLabel = tk.Label(janela, text='Magnitude da momento aplicada:')
    momentoLabel.grid(row=0, column=0, padx=5, sticky=tk.W)
    
    # momento entry
    momentoEntry = tk.Entry(janela, textvariable=momentoVar, borderwidth=5, relief=tk.FLAT)
    momentoEntry.grid(row=1, column=0, padx=5, pady=5)

    sliderLabel = tk.Label(janela, text='Posição:')
    sliderLabel.grid(row=2, column=0, padx=2, sticky=tk.W)

    # slider
    sliderVar = tk.DoubleVar()
    slider = tk.Scale(janela, from_=0, to=moduloTan(num, canvas, lines)[0], variable=sliderVar, orient='horizontal')
    slider.grid(row=3, column=0, ipadx=50)

    aplicar = tk.Button(janela, text="Adicionar momento", command=lambda: addImageAndArray(num, momentos, canvas, sliderVar, lines, theta, janela, momentoVar))
    aplicar.grid(row=4, column=0, padx=5, columnspan=2, pady=5, sticky=tk.W)
    
    vinculoButton = tk.Button(janela, text=("↩️ Reverter"), 
                                      command=lambda: deleteVinculo(momentos[num][len(momentos[num]) - 1], momentos, canvas, len(momentos[num]), janela, num, 1))
    vinculoButton.grid(row=0, column=1, padx=40, pady=5, sticky=tk.EW)
    
    spacer2 = tk.Label(janela, text="")
    spacer2.grid(row=9, column=0, columnspan=3)


def addImageAndArray(num, momentos, canvas, sliderVar, lines, theta, janela, momentoVar):
    if momentoVar.get() == '':
        messagebox.showerror("Erro", "Momento precisa ter um valor!")
        return
    
    slider = sliderVar.get()

    newX = slider*(math.cos(np.deg2rad(theta)))
    newY = slider*(math.sin(np.deg2rad(theta)))

    newX = canvas.coords(lines[num])[0] + newX
    newY = canvas.coords(lines[num])[1] - newY
    canvas.coords(momentos, newX, newY)
    imagem = adicionarMomento(newX, newY, canvas)

    momentos[num].append([(newX, newY), imagem, momentoVar.get()])
   

def addVinculo(num, theta, canvas, lines, vinculos, janela):
    janela = Toplevel(janela)
    janela.title("Adicionar vínculo {}".format(num + 1))
    janela.geometry('680x360')
    janela.minsize(340, 180)
    janela.maxsize(420, 280)
    
    x = canvas.coords(lines[num])[0]
    y = canvas.coords(lines[num])[1]

    # vinculos
    # selection box label
    selectionLabel = tk.Label(janela, text='Tipo de vínculo:')
    selectionLabel.grid(row=0, column=0, padx=2, sticky=tk.W)
    
    selectionVar = tk.StringVar(janela)
    options = ["Apoio Simples", "Apoio Duplo", "Engaste"]
    default_value = options[0]

    selectionVar.set(default_value)

    selectionBox = tk.OptionMenu(janela, selectionVar, *options)
    selectionBox.grid(row=1, column=0, padx=40, pady=5, sticky=tk.EW)

    buttons = []
    # slider label
    sliderLabel = tk.Label(janela, text='Posição:')
    sliderLabel.grid(row=2, column=0, padx=2, sticky=tk.W)
    
    # slider
    sliderVar = tk.DoubleVar()
    slider = tk.Scale(janela, from_=0, to=moduloTan(num, canvas, lines)[0], variable=sliderVar, orient='horizontal')
    slider.grid(row=3, column=0, ipadx=50)

    aplicar = tk.Button(janela, text="Adicionar vínculo", command=lambda: addVinculoImageAndArray(num, vinculos, selectionVar, canvas, sliderVar, lines, theta, janela, buttons))
    aplicar.grid(row=4, column=0, padx=5, columnspan=2, pady=5, sticky=tk.W)
    vinculoButton = tk.Button(janela, text=("↩️ Reverter"), 
                                      command=lambda: deleteVinculo(vinculos[num][len(vinculos[num]) - 1], vinculos, canvas, len(vinculos[num]), janela, num, 2))
    vinculoButton.grid(row=0, column=1, padx=40, pady=5, sticky=tk.EW)
    
        
def deleteVinculo (vinculo, vinculos, canvas, index, janela, num, index2):
    canvas.delete(vinculos[num][len(vinculos[num]) - 1][index2])
    i = 1
    aux = [[]]
    for vinculo in vinculos[num]:
        if i != index:
            aux.append(vinculo)
        i += 1
    vinculos[num] = aux


def addVinculoImageAndArray(num, vinculos, type, canvas, sliderVar, lines, theta, janela, buttons):
    slider = sliderVar.get()

    newX = slider*(math.cos(np.deg2rad(theta)))
    newY = slider*(math.sin(np.deg2rad(theta)))

    newX = canvas.coords(lines[num])[0] + newX
    newY = canvas.coords(lines[num])[1] - newY
    
    canvas.coords(vinculos, newX, newY)
    imagem = ""
    if type.get() == "Apoio Simples":
        imagem = adicionarApoioSimples(newX, newY, canvas)
    elif type.get() == "Apoio Duplo":
        imagem = adicionarArticulacao(newX, newY, canvas)
    elif type.get() == "Conexao":
        imagem = adicionarJuncao(newX, newY, canvas)
    else:
        imagem = adicionarEngaste(newX, newY, canvas)
    vinculos[num].append([(newX, newY), type.get(), imagem])
    
    
def moduloTan (num, canvas, lines):
    a = canvas.coords(lines[num])[2] - canvas.coords(lines[num])[0]
    b = canvas.coords(lines[num])[1] - canvas.coords(lines[num])[3]
    modulo = math.hypot(a, b)

    if a == 0 and b > 0:
        tan = 90
    elif b == 0 and a < 0: 
        tan = 180
    elif b == 0 and a > 0: 
        tan = 0
    elif a == 0 and b < 0: 
        tan = 270
    else:
        tan = abs(np.rad2deg(math.atan(b/a)))
        
    if b > 0 and a < 0:
        tan = np.rad2deg(math.atan(b/a)) + 180
    elif b < 0 and a < 0:
        tan += 180
    elif b < 0 and a > 0:
        tan = 360 - tan
    
    return (modulo, tan)


def anguloForca (canvas, forcas):
    dx = canvas.coords(forcas)[2] - canvas.coords(forcas)[0]
    dy = canvas.coords(forcas)[1] - canvas.coords(forcas)[3]
    modulo = math.hypot(dx, dy)
    tan = 0

    if dx == 0:
        tan = 90

    else:
        tan = np.rad2deg(math.atan(dy/dx))

    if dx > 0 and dy > 0:
        tan += 180
    elif dx > 0 and dy == 0:
        tan = 180
    elif dx > 0 and dy < 0:
        tan += 180
    elif dx == 0 and dy > 0:
        tan += 180
    elif dx < 0 and dy > 0:
        tan += 360
    elif dx < 0 and dy == 0:
        tan = 0

    return (modulo, tan)


def addForca(num, theta, canvas, lines, forcas, janela):
    janela = Toplevel(janela)
    janela.title("Forca aplicada da barra {}".format(num + 1))
    janela.geometry('480x360')
    janela.minsize(360, 180)
    janela.maxsize(480, 280)
    
    x = canvas.coords(lines[num])[0]
    y = canvas.coords(lines[num])[1]
    
    if canvas.coords(forcas)[0] == 0:
        canvas.coords(forcas, x, y-100, x, y)


    # forca label
    forcaVar = tk.StringVar()
    forcaLabel = tk.Label(janela, text='Magnitude da forca aplicada:')
    forcaLabel.grid(row=0, column=0, padx=5, sticky=tk.W)
    
    # forca entry
    forcaEntry = tk.Entry(janela, textvariable=forcaVar, borderwidth=5, relief=tk.FLAT)
    forcaEntry.insert(0, "{:.2f}".format(anguloForca(canvas, forcas)[0]))
    forcaEntry.grid(row=1, column=0, padx=5, pady=5)
    
    # slider label
    sliderLabel = tk.Label(janela, text='Posição:')
    sliderLabel.grid(row=2, column=0, padx=2, sticky=tk.W)
    
    # slider
    sliderVar = tk.DoubleVar()
    slider = tk.Scale(janela, from_=0, to=moduloTan(num, canvas, lines)[0], variable=sliderVar, orient='horizontal')
    slider.grid(row=3, column=0, ipadx=50)
    
    # aplicar forca button
    aplicar = tk.Button(janela, text="Aplicar Força", 
                        command=lambda: aplicarForca(num, theta, forcaVar, sliderVar, 
                                                     canvas, forcas, lines))
    aplicar.grid(row=4, column=0, padx=5, columnspan=2, pady=5, sticky=tk.W)
    
    # angulo da forca label
    anguloVar = tk.StringVar()
    anguloLabel = tk.Label(janela, text='Angulo da forca:')
    anguloLabel.grid(row=0, column=1, padx=5, sticky=tk.W)
    
    # angulo entry
    anguloEntry = tk.Entry(janela, textvariable=anguloVar, borderwidth=5, relief=tk.FLAT)
    anguloEntry.insert(0, "{:.2f}".format(anguloForca(canvas, forcas)[1]))
    anguloEntry.grid(row=1, column=1, padx=5, pady=5)
    
    # aplicar angulo button
    aplicar = tk.Button(janela, text="Aplicar Angulo", command=lambda: mudarAnguloForcas(forcas, canvas, anguloVar))
    aplicar.grid(row=2, column=1, padx=5, columnspan=2, pady=5, sticky=tk.W)
    
    
def mudarAnguloForcas(forcas, canvas, anguloVar):
    x = float(canvas.coords(forcas)[0])
    y = float(canvas.coords(forcas)[1])
    x2 = float(canvas.coords(forcas)[2])
    y2 = float(canvas.coords(forcas)[3])
    r = float(anguloForca(canvas, forcas)[0])
    
    inputAngle = float(anguloVar.get()) 
    newX = r*(math.cos(np.deg2rad(-inputAngle)))
    newY = r*(math.sin(np.deg2rad(-inputAngle)))

    x = x2 + newX
    y = y2 + newY
  
    canvas.coords(forcas, x, y, x2, y2)
    
    
def aplicarForca(num, theta, forca, sliderVar, canvas, forcas, lines):
    slider = sliderVar.get()
    try:
        forca = float(forca.get())
    except:
        forca = 100
        
    if forca == 0:
        canvas.coords(forcas, 0, 0, 0, 0)
        return

    newX = slider*(math.cos(np.deg2rad(theta)))
    newY = slider*(math.sin(np.deg2rad(theta)))

    newX = canvas.coords(lines[num])[0] + newX
    newY = canvas.coords(lines[num])[1] - newY
    
    canvas.coords(forcas, newX, newY-forca, newX, newY)
    
    
def mudarCoords(num, x, y, x2, y2, r, theta, canvas, lines, rEntry, thetaEntry, forcas, vinculos):
    x = float(x.get()) 
    y = float(y.get())
    x2 = float(x2.get())
    y2 = float(y2.get())
    r = float(r.get())
    theta = float(theta.get())
    
    canvas.coords(lines[num], x, y, x2, y2)
    mt = moduloTan(num, canvas, lines)
    updateModuloTan(mt[0], mt[1], rEntry, thetaEntry)
    
    canvas.coords(forcas[num]["f1"], 0, 0, 0, 0)
    canvas.coords(forcas[num]["f2"], 0, 0, 0, 0)
    canvas.coords(forcas[num]["f3"], 0, 0, 0, 0)


def mudarPol(num, x, y, x2, y2, r, theta, canvas, lines, xEntry, yEntry, x2Entry, y2Entry, forcas, vinculos):
    x = float(x.get()) 
    y = float(y.get())
    x2 = float(x2.get())
    y2 = float(y2.get())
    r = float(r.get())
    theta = float(theta.get())

    theta = 360 - theta
    newX = r*(math.cos(np.deg2rad(theta)))
    newY = r*(math.sin(np.deg2rad(theta)))

    x2 = x + newX
    y2 = y + newY
        
    theta = 360 - theta
    canvas.coords(lines[num], x, y, x2, y2)
    
    updateCoords(x, y, x2, y2, xEntry, yEntry, x2Entry, y2Entry)
    
    canvas.coords(forcas[num]["f1"], 0, 0, 0, 0)
    canvas.coords(forcas[num]["f2"], 0, 0, 0, 0)
    canvas.coords(forcas[num]["f3"], 0, 0, 0, 0)


def updateModuloTan(modulo, tan, rEntry, thetaEntry):
    rEntry.delete(0, END)
    rEntry.insert(0, "{:.2f}".format(modulo))
    
    thetaEntry.delete(0, END)
    thetaEntry.insert(0, "{:.2f}".format(tan))
    
    
def updateCoords(x, y, x2, y2, xEntry, yEntry, x2Entry, y2Entry):
    xEntry.delete(0, END)
    xEntry.insert(0, "{:.2f}".format(x))
    
    yEntry.delete(0, END)
    yEntry.insert(0, "{:.2f}".format(y))
    
    x2Entry.delete(0, END)
    x2Entry.insert(0, "{:.2f}".format(x2))
    
    y2Entry.delete(0, END)
    y2Entry.insert(0, "{:.2f}".format(y2))
    

def excluirBarra(num, janela, canvas, botaoBarra, lines, forcas, vinculos):
    global botaoCoord
    global botaoNum
    canvas.delete(lines[num])
    lines[num] = None
    botaoBarra[num].destroy()
    botaoBarra[num] = None
    janela.destroy()
    canvas.delete(forcas[num]["f1"])
    canvas.delete(forcas[num]["f2"])
    canvas.delete(forcas[num]["f3"])
    try:
        for vinculo in vinculos[num]:
            if vinculo != []:
                canvas.delete(vinculo[2])
    except:
        pass
    
    forcas[num]["f1"] = None
    forcas[num]["f2"] = None
    forcas[num]["f3"] = None

    botaoCoord = {"relx":0.01, "rely":0.25}

    for i in range(botaoNum):
        if type(botaoBarra[i]) != type(None):
            botaoBarra[i].config(text="Botao {}".format(i + 1))
            botaoBarra[i].place(relx=botaoCoord["relx"], rely=botaoCoord["rely"], relwidth=0.05, relheight=0.04, anchor='w')        
            botaoCoord["relx"] += 0.06 
            if (botaoCoord["relx"] > 0.14):
                botaoCoord["relx"] = 0.01
                botaoCoord["rely"] += 0.06
    
main()