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
cont = 0
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
        similaridade.append(contador.index(contador[c]))
if len(similaridade) == 1:
    if len(similaridade) == 1:
        for d in range(len(data)):
            if data[d][0] == users_film[contador.index(max(contador))] and data[d][1] == filme:
                print(f'A nota para o filme {filme} de acordo com a similarida é: {data[d][2]}')