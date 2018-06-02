import numpy as np

# lendos as dimensões das matrizes
M, N, P = tuple(map(int, input().split()))

# alocando as matrizes
# que serão concatenadas
m1 = np.zeros((N, P), int)
m2 = np.zeros((M, P), int)

# lê as N primeiras linhas
for i in range(N):
    m1[i] = np.array(input().split(), int)

# lê as M últimas linhas
for i in range(M):
    m2[i] = np.array(input().split(), int)
    
print(np.concatenate((m1, m2), axis=0))