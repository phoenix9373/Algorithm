n = int(input())

def fibo(x):
    f = [0, 1] # 기저
    for i in range(2, x+1):
        f.append(f[i-1] + f[i-2])
    return f[x]
print(fibo(n))

# 4: 3, 2 / 3: 2, 1 / 2: 1, 0 / 2: 1, 0 -> (3, 2)
# 3: 2, 1 / 2: 1, 0 -> (2, 1)
# 2: 1, 0 -> (1, 1)