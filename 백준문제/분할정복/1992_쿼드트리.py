N = int(input())
arr = [' '.join(input()).split() for _ in range(N)]


def sol(x, y, n):
    if n == 1:
        return arr[x][y]

    r1 = sol(x, y, n // 2)
    r2 = sol(x + n // 2, y, n // 2)
    r3 = sol(x, y + n // 2, n // 2)
    r4 = sol(x + n // 2, y + n // 2, n // 2)

    if r1 == r2 == r3 == r4 and len(r1) == 1:
        return r1
    else:
        return f'({r1 + r3 + r2 + r4})'


ans = sol(0, 0, N)
print(ans)