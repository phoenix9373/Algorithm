'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

V = int(input())
tmp = list(map(int, input().split()))

arr = [[i] if i != 0 else [] for i in range(V + 1)]

for i in range(V - 1):
    s, e = tmp[i*2] ,tmp[i*2 + 1]
    arr[s].append(e)

for k in range(1, V + 1):
    while len(arr[k]) != 3:
        arr[k].append(0)

result = []


def preorder(T): # T는 arr[1]
    if T: # None이 아니면
        result.append(T[0])
        preorder(arr[T[1]])
        preorder(arr[T[2]])


def inorder(T): # T는 arr[1]
    if T: # None이 아니면
        preorder(arr[T[1]])
        result.append(T[0])
        preorder(arr[T[2]])


def postorder(T): # T는 arr[1]
    if T: # None이 아니면
        preorder(arr[T[1]])
        preorder(arr[T[2]])
        result.append(T[0])


preorder(arr[1])
print(*result)