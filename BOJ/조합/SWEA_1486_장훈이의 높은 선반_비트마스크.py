T = int(input())

for tc in range(1, T+1):
    N, B = map(int, input().split())

    H = list(map(int, input().split()))

    ans = pow(2, 20)

    for i in range(1, 1<<N):
        total = 0
        for j in range(N):
            if i & (1<<j):
                total += H [j]

        if total >= B and total < ans:
            ans = total

    print('#{} {}'.format(tc, ans - B))