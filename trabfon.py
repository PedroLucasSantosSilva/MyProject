u_data = open('u.data', 'r').readlines()
u_item = open('u.item', 'r').readlines()
user = str(input('Digite o usuário:'))
data = []
item = []
filmes_user = []
users_sem = []
desc = []
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
            users_sem.append([data[z][0]])

for u in range(len(users_sem)):
    for l in range(len(data)):
        if users_sem[u] == data[l][0]:
            for c in range(len(filmes_user)):
                if data[l][1] == filmes_user[c]:
                    cont += 1
    users_sem[u].append(cont)
print(users_sem)
