# encoding: utf-8
L = [11, 2, 31, 4, 51, 8, 19]
for i in range(len(L) - 1):
    for j in range(len(L) - 1 - i):
        if L[j] > L[j+1]:
            L[j], L[j+1] = L[j+1], L[j]
print(L)
