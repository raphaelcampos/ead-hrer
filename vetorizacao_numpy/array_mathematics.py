import numpy as np

N, M = tuple(map(int, input().split()))

A = np.zeros((N, M), int)
B = np.zeros((N, M), int)

for i in range(N):
    A[i] = np.array(input().split(), int)
    
for i in range(N):
    B[i] = np.array(input().split(), int)
    
print(A + B)
print(A - B)
print(A * B)
print(A // B)
print(A % B)
print(A ** B)