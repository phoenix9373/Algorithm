# 부분 집합 만드는 방법

# 어떻게 해야할까요?? 10개의 값이 있는데 어떻게 할까?

# 재귀로 하면 하나의 깊이에서 하나씩 선택.

arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
n = len(arr)

# 총 2^n개의 부분집합이 있으므로.
for i in range(1<<n): # n번 좌측으로. 2 ^ n
    # 여기서 4번 연산해야한다. 2 ^ 4 이므로.
    tmp = []
    for j in range(n - 1, -1, -1):
        if i & (1<<j):
            tmp.append(arr[j])
    if sum(tmp) == 0:
        print(tmp)