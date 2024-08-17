A = [1, 5, 7, 8, 4, 47, 9 ,0]

for i in range(1, len(A)):
    key = A[i]
    j = i - 1
    while A[j] > key and j >= 0:
        A[j+1] = A[j]
        j = j - 1
    A[j + 1] = key
    
print(A)