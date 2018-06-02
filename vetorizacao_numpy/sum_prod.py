import numpy as np

N, M = tuple(map(int, input().split()))

m = np.zeros((N, M), int)

for i in range(N):
    m[i] = np.array(input().split(), int)
    
print(m.sum(axis=0).prod())