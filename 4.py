matriz = []
maximo = []
minimo = []

linhas = int(input('Digite a quantidade de linhas da matriz:'))
colunas = int(input('Digite a quantidade de colunas da matriz:'))
for l in range(0, linhas):
    line = []
    for c in range(0, colunas):
        elemento = (int(input(f'Digite um número para a posição[{l}, {c}]:')))
        line.append(elemento)
    maximo.append(max(line))
    minimo.append(min(line))
    matriz.append(line)

for l in range(0, linhas):
    for c in range(0, colunas):
            print(f'[{matriz[l][c]:^5}]', end='')
    print()
for i in range(len(maximo)):
    print(f'O maior valor da linha {i + 1} é: {maximo[i]}')
    print(f'O menor valor da linha {i + 1} é: {minimo[i]}')