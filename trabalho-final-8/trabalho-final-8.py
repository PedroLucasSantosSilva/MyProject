from tkinter import *

def netflix():
    u_data = open('u.data', 'r').readlines()
    u_item = open('u.item', 'r').readlines()
    user = str(user1.get())
    data = []
    item = []
    nome_f = ''
    filmes_user = []
    users_film = []
    filmes_users = []
    aux_users = []
    contador = []
    similaridade = []
    maximos = []
    cont2 = 0
    menor = 0
    for i in range(len(u_data)):
        a = u_data[i]
        a = a.split()
        data.append(a)
    for i in range(len(u_item)):
        b = u_item[i]
        b = b.split('|')
        item.append(b)

    for j in range(len(u_data)):
        if user == data[j][0]:
            filmes_user.append(data[j][1])

    filme = str(filme1.get())
    for f in range(len(item)):
        if filme == item[f][0]:
            nome_f = item[f][1]

    if filme not in filmes_user:
        for z in range(len(data)):
            if data[z][1] == filme:
                users_film.append(data[z][0])

        for n in range(len(users_film)):
            for m in range(len(data)):
                if users_film[n] == data[m][0]:
                    aux_users.append(data[m][1])
            filmes_users.append(aux_users[:])
            aux_users.clear()

        for a in range(len(filmes_users)):
            cont = 0
            for b in range(len(filmes_users[a])):
                if filmes_users[a][b] in filmes_user:
                    cont += 1
            contador.append(cont)
        for c in range(len(contador)):
            if max(contador) == contador[c]:
                maximos.append(contador[c])

        if len(maximos) == 1:
            for d in range(len(data)):
                if data[d][0] == users_film[contador.index(max(contador))] and data[d][1] == filme:
                    result["text"] = f'A nota para: {filme} | "{nome_f}", de acordo com a similaridade é: {data[d][2]}.'
        else:
            for e in range(len(contador)):
                for f in range(len(data)):
                    if data[f][0] == users_film[contador.index(contador[e])] and data[f][1] == filme\
                            and contador[e] in maximos:
                        for g in range(len(filmes_user)):
                            for h in range(len(data)):
                                if data[f][1] == filmes_user[g] and data[h][0] == user and\
                                            data[f][0] == users_film[contador.index(contador[e])]:
                                    n1 = int(data[h][2])
                                    n2 = int(data[f][2])
                                    cont2 += abs(n1 - n2)
                                if h == 0:
                                    menor = cont2
                                    similaridade.append(data[f])
                                    cont2 = 0
                                else:
                                    if menor > cont2:
                                        menor = cont2
                                        similaridade.clear()
                                        similaridade.append(data[f])
                                        cont2 = 0
            result["text"] = f'A nota para: {filme} | "{nome_f}", de acordo com a similaridade é: {similaridade[0][2]}.'
    else:
        result["text"] = 'Filme já assistido!'
def clear():
    result["text"] = ""


window = Tk()

window.title("Projeto 8")
window.geometry('600x400+400+200')
window['bg'] = '#262626'

inicio = Label(window, text="Trabalho 8: Recomendação de Filmes", font="Arial 15 bold")
inicio['bg'] = '#262626'
inicio['fg'] = '#c0c0c0'
inicio.pack()

img = PhotoImage(file="netflix2.png")
imagem = Label(image=img)
imagem['bg'] = '#262626'
imagem.pack()

texto_user = Label(window, text="Digite a identificação do usuário:", font="Arial 13")
texto_user['bg'] = '#262626'
texto_user['fg'] = '#c0c0c0'
texto_user.pack()

user1 = Entry(window)
user1['bg'] = '#e7ffff'
user1['fg'] = '#000'
user1.pack(padx=10, pady=10)

texto_filme = Label(window, text="Digite a identificação do filme:", font="Arial 13")
texto_filme['bg'] = '#262626'
texto_filme['fg'] = '#c0c0c0'
texto_filme.pack()

filme1 = Entry(window)
filme1['bg'] = '#e7ffff'
filme1['fg'] = '#000'
filme1.pack(padx=10, pady=10)

botao = Button(window, text="Verificar", comman=netflix)
botao['bg'] = '#a50000'
botao['fg'] = '#f8f8ff'
botao.pack()

result = Label(window, text="", font="Arial 11")
result['bg'] = '#262626'
result['fg'] = '#c0c0c0'
result.pack(padx=5, pady=5)

botao2 = Button(window, text="Limpar", command=clear)
botao2['bg'] = '#a50000'
botao2['fg'] = '#f8f8ff'
botao2.pack()

window.mainloop()
