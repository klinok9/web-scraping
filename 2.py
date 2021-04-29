# N = input('Введите массив:')
# N = N.split()
# N = [int(i) for i in N]
# for i in range(len(N)//2):
#     b = N[i]
#     N[i] = N[len(N)-i-1]
#     N[len(N)-i-1] = b
#
# print(N)

# a = input()
# a = a.split()
# a = [int(i) for i in a]
# for i in range(len(a)//2):
#     b = a[i]
#     a[i] = a[len(a)-i-1]
#     a[len(a)-i-1] = b
# #a.reverse()
# #a = a[::-1]
# print(a)

# from random import random
# N = input('Введите массив:')
# arr = [0] * N
# for i in range(N):
#     arr[i] = int(random() * 100)
# print(arr)
# m = 0
# for i in range(2,N,2):
#     if arr[i] > arr[m]:
#         m = i
# print(m,'-',arr[m])

from random import random
N = int(input())
arr = [0] * N
mx = 0
for i in range(N):
    arr[i] = random()
    print("%.2f" % arr[i], end='; ')
    if arr[i] > arr[mx]:
        mx = i
print("\narr[%d] = %.2f" % (mx, arr[mx]))
