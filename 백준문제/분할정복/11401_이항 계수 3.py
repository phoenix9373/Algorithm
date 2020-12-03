def sol(a, b):
    if b == 0:
        return 1
    if b % 2:
        return (sol(a, b // 2) ** 2 * a) % p
    else:
        return (sol(a, b // 2) ** 2) % p


N, K = map(int, input().split())

p = 1000000007

fact = [1 for _ in range(N + 1)]
for i in range(2, N + 1):
    fact[i] = fact[i - 1] * i % p

A = fact[N]
B = (fact[N - K] * fact[K]) % p

print((A % p) * (sol(B, p - 2) % p) % p)