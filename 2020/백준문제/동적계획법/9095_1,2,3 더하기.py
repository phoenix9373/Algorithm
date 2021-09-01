T = int(input())


def fibo(n):
    f = [0, 1, 2, 4]

    if n < 4:
        return f[n]

    for i in range(4, n + 1):
        f.append(f[i - 1] + f[i - 2] + f[i - 3])
    return f[-1]


for _ in range(T):
    N = int(input())
    print(fibo(N))