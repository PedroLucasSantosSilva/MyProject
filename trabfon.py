u_data = open('u.data', 'r').readlines()
u_item = open('u.item', 'r').readlines()
user = str(input('Digite o usuário:'))
data = []
item = []
filmes_user = []
users_sem = []
cont = []
ajuda = []
filmes_users = []
lista_sem = []
for i in range(len(u_data)):
    a = u_data[i]
    a = a.split()
    data.append(a)
for i in range(len(u_item)):
    b = u_item[i]
    b = b.split()
    item.append(b)

for j in range(len(u_data)):
    if user == data[j][0]:
        filmes_user.append(data[j][1])
filme = str(input('Digite o filme:'))
for z in range(len(data)):
    if data[z][1] == filme:
        for u in range(len(filmes_user)):
            if data[z][1] not in filmes_user[u]:
                cont.append(data[z][1])
                ajuda.append(data[z][0])
                if len(filmes_users) <= len(cont):
                    filmes_users.clear()
                    filmes_users.append(cont[:])
                    users_sem.clear()
                    users_sem.append(ajuda[0])
                    cont.clear()
                    ajuda.clear()
                elif len(users_sem) > len(cont):
                    cont.clear()
                    ajuda.clear()
            else:
                print('Filme já assistido')
                break

for r in range(len(data)):
    if data[r][0] == users_sem[0]:
        lista_sem.append(data[r])
print(lista_sem)
