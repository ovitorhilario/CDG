from omr import *
from tkinter import *

app = Tk()
app.title('Perguntas Iniciais')
app.geometry('380x240')
app.resizable(False, False)

#### FRAME 2 ###

def frame2():
    app.geometry('300x400')
    app.title('Preencha o Gabarito')
    Frame2 = Frame(app)
    Frame2.pack(pady=20)

    nQ = vnQuestions.get()  # NÚMERO DE QUESTOES
    nA = vnAnswer.get()  # NÚMERO DE RESPOSTAR P/ QUESTAO
    nC = vncan.get()  # NÚMERO DA CAMERA

    listnAnswer = ['A', 'B', 'C', 'D', 'E']
    x = slice(int(nA))
    listnAnswer = listnAnswer[x]
    vFeedback = []
    AnswersList = []
    CanValue = int(nC) - 1

    for i in range(int(nQ)):
        n = i + 1
        vFeedback.append(StringVar())
        vFeedback[i].set(listnAnswer[0])
        Label(Frame2, text=n).grid(row=i, column=0)
        OptionMenu(Frame2, vFeedback[i], *listnAnswer).grid(row=i, column=1)

    def show():
        for i in range(len(vFeedback)):
            a = vFeedback[i].get()
            b = 0
            if (a == 'A'):
                b = 0
            elif (a == 'B'):
                b = 1
            elif (a == 'C'):
                b = 2
            elif (a == 'D'):
                b = 3
            elif (a == 'E'):
                b = 4
            AnswersList.append(int(b))

        resCan = []
        num = int(listCanProp.index(vCanProp.get()))

        if (num == 0):
            resCan = [700, 700]
        elif (num == 1):
            resCan = [960, 720]
        elif (num == 2):
            resCan = [900, 720]
        elif (num == 3):
            resCan = [1280, 720]
        elif (num == 4):
            resCan = [960, 600]

        app.destroy()
        program(AnswersList, int(nQ), int(nA), CanValue, resCan)

    Button(Frame2, text='Prosseguir', command=show).grid(row=10, column=3, sticky=E, padx=20, pady=5)

#### FRAME 1 ###

Frame1 = Frame(app)
Frame1.pack(pady=10)

def nextFrame():
    Frame1.destroy()
    frame2()

# --- NÚMERO DE QUESTÕES POR TESTE

listnQuestions = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
vnQuestions = StringVar()
vnQuestions.set(listnQuestions[9])

Label(Frame1, text='Número de questões do teste:').grid(row=0, column=0, sticky=W, padx=10, pady=5)
OptionMenu(Frame1, vnQuestions, *listnQuestions).grid(row=0, column=1, sticky=E, padx=10, pady=5)

# --- NÚMERO DE RESPOSTAS POR QUESTÃO

listnAnswer = ['1', '2', '3', '4', '5']
vnAnswer = StringVar()
vnAnswer.set(listnAnswer[4])

Label(Frame1, text='Número de respostas por questão:').grid(row=1, column=0, sticky=W, padx=10, pady=5)
OptionMenu(Frame1, vnAnswer, *listnAnswer).grid(row=1, column=1, sticky=E, padx=10, pady=5)

# --- OPÇÃO DE ENTRADA DA CAMERA

listncan = ['1', '2', '3']
vncan = StringVar()
vncan.set(listncan[0])

ncan = Label(Frame1, text='Opção de entrada da Camera:').grid(row=2, column=0, sticky=W, pady=10, padx=10)
ncanop = OptionMenu(Frame1, vncan, *listncan).grid(row=2, column=1, sticky=E, padx=10, pady=5)

# --- RESOLUÇÃO DA CAMERA

listCanProp = ['1:1', '4:3', '5:4', '16:9', '16:10']
vCanProp = StringVar()
vCanProp.set(listCanProp[0])

CanProp = Label(Frame1, text='Proporção da Imagem da Camera:').grid(row=3, column=0, sticky=W, pady=10, padx=10)
CanPropOp = OptionMenu(Frame1, vCanProp, *listCanProp).grid(row=3, column=1, sticky=E, padx=10, pady=5)

# --- PROSSEGUIR

Button(Frame1, text='Prosseguir', command=nextFrame).grid(row=4, column=1, sticky=E, padx=10, pady=10)

# --- APP LOOP

app.mainloop()

