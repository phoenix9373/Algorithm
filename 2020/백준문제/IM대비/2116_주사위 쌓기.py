from copy import deepcopy
N = int(input())

arr_list = [list(map(int, input().split())) for _ in range(N)]
res = 0
# 0, 5 - A, F
# 1, 3 - B, D
# 2, 4 - C, E

idx_list = [5, 3, 4, 1, 2, 0]
for k in range(6):
    arr = deepcopy(arr_list)
    tmp = arr[0][k]
    value = 0
    for i in range(N):
        idx = arr[i].index(tmp)
        arr[i][idx] = 0
        tmp = arr[i][idx_list[idx]]
        arr[i][idx_list[idx]] = 0
        value += max(arr[i])
    if value > res:
        res = value

print(res)
