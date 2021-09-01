N = int(input())


def fibo(n):
    if n == 1:
        return 1
    f = [1, 1]

    for i in range(2, N + 1):
        f.append(f[i - 1] + 2 * f[i - 2])
    return f[-1] % 10007


print(fibo(N))
