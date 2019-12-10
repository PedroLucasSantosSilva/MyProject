u_data = open('u.data', 'r').readlines()
u_item = open('u.item', 'r').readlines()
user = str(input('Digite o usuário:'))
data = []
item = []
filmes_user = []
users_sem = []
dados_users = []
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
            users_sem.append([data[z][0]])

for u in range(len(users_sem)):
    for l in range(len(data)):
        if users_sem[u] == data[l][0] and data[l][1] != filme:
            dados_users.append(data[l])

for h in range(len(filmes_user)):
    for c in range(len(dados_users)):
        cont = 0
        if dados_users[c][1] == filmes_user[h]:
            cont += 1
        for a in range(len(users_sem)):
            if dados_users[c][0] == users_sem[a]:
                users_sem[a].append(cont)
print(users_sem)
