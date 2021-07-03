# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np
import math
import matplotlib.pyplot as mpl
from numpy.matrixlib.defmatrix import matrix
from sympy import *
import copy
from sympy.utilities.lambdify import lambdastr
x1, x2, x3, x4, x5 = symbols('x1, x2, x3, x4, x5')

# %%
linha_1 = [1, 1, 1, 0, 2]
linha_2 = [0, 1, 2, 1, 1]
linha_3 = [0, 0, 1, 2, 1]
linha_4 = [0, 0, 0, 2, 1]
linha_5 = [0, 0, 0, 0, 10]

matriz = Matrix([linha_1, linha_2, linha_3, linha_4, linha_5])
matriz

# %%
linha_x = Matrix([[x1],[x2],[x3],[x4],[x5]])
linha_x

# %%
linha_r = Matrix([[1],[2],[-2],[-4],[-20]])
linha_r

# %%
solve(Eq(matriz * linha_x , linha_r), [x1, x2, x3, x4, x5])

# %%
linha_1 = [1, 0, 0, 0, 0]
linha_2 = [1, 1, 0, 0, 0]
linha_3 = [1, 2, 1, 0, 0]
linha_4 = [1, 1, 2, 2, 0]
linha_5 = [-2, -1, 0, -3, 10]

matriz = Matrix([linha_1, linha_2, linha_3, linha_4, linha_5])
matriz
# %%
linha_x = Matrix([[x1],[x2],[x3],[x4],[x5]])
linha_x

# %%
linha_r = Matrix([[1],[3],[6],[9],[0]])
linha_r

# %%
solve(Eq(matriz * linha_x , linha_r), [x1, x2, x3, x4, x5])

# %%
linha_1 = [2, 1, 3, 4]
linha_2 = [1, 4, 2, 1]
linha_3 = [3, 2, 1, 4]
linha_4 = [2, 2, 3, 1]

matriz = Matrix([linha_1, linha_2, linha_3, linha_4])
matriz

# %%
linha_x = Matrix([[x1],[x2],[x3],[x4]])
linha_x

# %%
linha_r = Matrix([[16],[5],[11],[12]])
linha_r

# %%
linha_1 = [2]

matriz_A1 = Matrix([linha_1])
matriz_A1

# %%
matriz_A1.det()

# %%
linha_1 = [2, 1]
linha_2 = [1, 4]

matriz_A2 = Matrix([linha_1, linha_2])
matriz_A2

# %%
matriz_A2.det()

# %%
linha_1 = [2, 1, 3]
linha_2 = [1, 4, 2]
linha_3 = [3, 2, 1]

matriz_A3 = Matrix([linha_1, linha_2, linha_3])
matriz_A3

# %%
matriz_A3.det()

# %%
linha_1 = np.array([2, 1, 3, 4])
linha_2 = np.array([1, 4, 2, 1])
linha_3 = np.array([3, 2, 1, 4])
linha_4 = np.array([2, 2, 3, 1])

# %%    
matrix = [linha_1, linha_2, linha_3, linha_4]

def escalonamento(matrix):
    for index_pivo, linha_atual_pivo in enumerate(matrix):
        if index_pivo > len(matrix) - 2:
            break # Para se chegar a última linha
        for index, linha in enumerate(matrix):
            if index <= index_pivo:
                continue # Continua se for anterior ao pivo
            multiplicador = linha[index_pivo] / linha_atual_pivo[index_pivo]
            matrix[index] = linha - multiplicador * linha_atual_pivo
    return Matrix(matrix)

matriz = arredondar_matrix(escalonamento(matrix), 2)
matriz

# %%
for index, linha in enumerate(matrix):
    print(index, linha)
    for index_in, elemento_in in enumerate(linha):
        print(f'\t {index_in} {elemento_in}')
    print(linha[index])
    print()

# %%
