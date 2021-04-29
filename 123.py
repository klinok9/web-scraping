from random import randint

N = int(input("Введите N: "))


def massive(A):
    for row in A:
        for x in row:
            print("{:4}".format(x), end=" ")
        print()


A = [[0] * N for i in range(N)]
for i in range(N):
    for j in range(N):
        A[i][j] = randint(0, 20)
massive(A)
min = A[0][0]
for i in range(N):
    for j in range(i + 1):
        if A[i][N - 1 - i] < min:
            min = A[i][N - 1 - i]
print('min=', min)
