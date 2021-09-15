from tkinter import *

janela = Tk()

'''funçao pra pegar o valor do entry e transforma en inteiro e dps guarda em uma variavel pra depois somar
e substituir o valor do texto2 pelo da soma
'''

def calculo():
    print(caixa.get())
    num1 = int(caixa.get())
    num2 = int(caixa2.get())
    soma = num2 + num1
    texto1['text'] = 'resultado é', soma
    
#caixa que vai receber o primeiro valor
caixa = Entry(janela, width=25, bg='lime')
caixa.place(x=50, y=135)

#Caixa que vai receber o segundo valor
caixa2 = Entry(janela, width=25, bg='lime')
caixa2.place(x=50, y=165)

#criaçao do botao
bt = Button(janela, width=20, text="Clique", bg='lime', fg='black', command=calculo)
bt.place(x=50, y=100)

#criaçao de um texto que mostrara o resultado
texto1 = Label(janela, text="Resultado é:", bg='lime', fg='black', width=20)
texto1.place(x=50, y=60)

#criaçao do texto usado como Titulo, como fosse uma logo
texto2 = Label(janela, text="Caculadora de Adição", bg='lime', fg='black', width=20)
texto2.place(x=50, y=20)

#configuraçoes basicas
janela.title("Meu Programa")
janela.configure(bg='aqua')
janela.geometry("240x240")
janela.mainloop()
