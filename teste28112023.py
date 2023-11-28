# Calculadora de juros

# Apresentação
print('\n\t\t\t -- Calculadora de juros -- \n')

# Entradas
C = int(input('informe C: '))
I = int(input('informe I: '))
N = int(input('informe N: '))

# Processamento
total = C * I * N / 100

# Saida
print(f'{C} * {I} * {N} / {100} = {total}')


