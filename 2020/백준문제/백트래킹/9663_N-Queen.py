n, ans = int(input()), 0
a, b, c = [False] * n, [False] * (2 * n - 1), [False] * (2 * n - 1)


def sol(i):
    global ans
    if i == n:
        ans += 1
        return
    for j in range(n):
        if not (a[j] or b[i+j] or c[j-i+n-1]):
            a[j] = b[i + j] = c[j - i + n - 1] = True
            sol(i + 1)
            a[j] = b[i + j] = c[j - i + n - 1] = False


sol(0)
print(ans)