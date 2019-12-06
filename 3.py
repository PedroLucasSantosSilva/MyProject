matriz = []

linhas = int(input('Digite a quantidade de linhas da matriz:'))
colunas = int(input('Digite a quantidade de colunas da matriz:'))
for l in range(0, linhas):
    aux = []
    for c in range(0, colunas):
        aux.append(int(input(f'Digite um número para a posição[{l}, {c}]:')))
    matriz.append(aux[:])

for l in range(0, linhas):
    for c in range(0, colunas):
            print(f'[{matriz[l][c]:^5}]', end='')
    print()
for l in range(0, linhas):
    maior = 0
    menor = 0
    for c in range(0, colunas):
        if l == 0 and c == 0:
            maior = matriz[l][c]
            menor = matriz[l][c]
        elif matriz[l][c] < menor or menor == 0:
            menor = matriz[l][c]
        elif matriz[l][c] > maior:
            maior = matriz[l][c]
    print(f'O maior elemento da linha {l + 1} é: {maior}')
    print(f'O maior elemento da linha {l + 1} é: {menor}')