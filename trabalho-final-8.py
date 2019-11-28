u_data = open('u.data', 'r').readlines()
user = str(input('Digite o usuário:'))
filmes = []
users = []
for i in range(len(u_data)):
    a = u_data[i]
    a = a.split()
    if user == a[0]:
        filmes.append(a[1])
        for j in range(len(filmes)):
            if a[1] == filmes[j] and a[0] != user:
                users.append(a[0])