N = int(input())


def dp(n):
    f = [0, 0, 1, 1, 2]

    if n < 5:
        return f[n]

    for i in range(5, n + 1):
        a, b, c = pow(2, 30), pow(2, 30), pow(2, 30)
        if i % 3 == 0:
            a = f[int(i / 3)]
        if i % 2 == 0:
            b = f[int(i / 2)]
        c = f[i - 1]
        tmp = min(a, b, c)
        f.append(tmp + 1)
    return f[-1]


print(dp(N))
