matriz = []
aux = []
cont = 0
linhas = int(input('Digite a quantidade de linhas da matriz:'))
colunas = int(input('Digite a quantidade de colunas da matriz:'))
for l in range(0, linhas):
    for c in range(0, colunas):
        aux.append(int(input(f'Digite um número para a posição[{l}, {c}]:')))
    matriz.append(aux[:])
    aux.clear()
for l in range(0, linhas):
    for c in range(0, colunas):
            print(f'[{matriz[l][c]:^5}]', end='')
    print()
for l in range(0, linhas):
    for c in range(0, colunas):
        if matriz[l][c] % 2 != 0:
            cont += matriz[l][c]
print(f'A soma dos ímpares é {cont}')