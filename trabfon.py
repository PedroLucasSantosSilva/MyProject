u_data = open('u.data', 'r').readlines()
u_item = open('u.item', 'r').readlines()
user = str(input('Digite o usuário:'))
data = []
item = []
filmes_user = []
users_sem = []
desc = []
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
            if data[z][1] != filmes_user[u]:
                desc.append(data[z][0])
            else:
                break

for r in range(len(desc)):
    if desc[r] not in users_sem:
        users_sem.append(desc[r])
print(users_sem)
