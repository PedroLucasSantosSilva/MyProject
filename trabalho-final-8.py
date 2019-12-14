u_data = open('u.data', 'r').readlines()
u_item = open('u.item', 'r').readlines()
user = str(input('Digite o usuário:'))
data = []
item = []
filmes_user = []
users_film = []
filmes_users = []
aux_users = []
contador = []
similaridade = []
maximos = []
cont = 0
cont2 = 0
menor = 0
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

##print(users_film)
##for movies in filmes_users:
##print(movies)


for a in range(len(filmes_users)):
    for b in range(len(filmes_users[a])):
        if filmes_users[a][b] in filmes_user:
            cont += 1
    contador.append(cont)
    cont = 0
for c in range(len(contador)):
    if max(contador) == contador[c]:
        maximos.append(contador.index(contador[c]))
if len(maximos) == 1:
    if len(maximos) == 1:
        for d in range(len(data)):
            if data[d][0] == users_film[contador.index(max(contador))] and data[d][1] == filme:
                print(f'A nota para o filme {filme} de acordo com a similarida é: {data[d][2]}')
    else:
        for e in range(len(contador)):
            for f in range(len(data)):
                if data[f][0] == users_film[contador.index(contador[f])] and data[f][1] == filme:
                    for g in range(len(filmes_user)):
                        for h in range(len(data)):
                            if data[f][1] == filmes_user[g] and data[h][0] == user and data[f][0] == users_film[contador.index(contador[f])]:
                                n1 = int(data[h][2])
                                n2 = int(data[f][2])
                                cont2 += abs(n1 - n2)
                            if h == 0:
                                menor = cont2
                                similaridade.append(data[f])
                                cont2 = 0
                            else:
                                if cont2 > menor:
                                    menor = cont2
                                    similaridade.clear()
                                    similaridade.append(data[f])
                                    cont2 = 0
        print(f'A nota para o filme {filme} de acordo com a similarida é: {data[f][2]}')
