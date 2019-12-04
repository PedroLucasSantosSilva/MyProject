u_data = open('u.data', 'r').readlines()
u_item = open('u.item', 'r').readlines()
user = str(input('Digite o usuário:'))
data = []
item = []
filmes_user = []
users_sem = []
cont = []
filmes_users = []
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
                if filmes_user[u] != data[z][1]:
                    cont.append(data[z][1])
                    filmes_users.append(data[z][1])
                    if len(filmes_users) == len(cont):
                        users_sem = data[z][0]
                    elif len(filmes_users) > len(cont):
                        cont.clear()
                    else:
                        filmes_users.append(cont[:])

print(users_sem)