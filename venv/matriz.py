import numpy as np

# Cria uma matriz 3x3
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Percorre e imprime cada elemento
for linha in matriz:
    for elemento in linha:
        print(elemento, end=' ')
    print()
