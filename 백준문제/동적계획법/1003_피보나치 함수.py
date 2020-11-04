import sys
n = int(sys.stdin.readline())

def fibo_count(x):
    f = [[1, 0], [0, 1]]

    for i in range(2, x+1):
        f.append([f[i-1][0] + f[i-2][0], f[i-1][1] + f[i-2][1]])
    return f[x]

for i in range(n):
    k = int(sys.stdin.readline())
    print(*fibo_count(k))

# 4: 3, 2 / 3: 2, 1 / 2: 1, 0 / 2: 1, 0 -> (2, 3)
# 3: 2, 1 / 2: 1, 0 -> (1, 2)
# 2: 1, 0 -> (1, 1)