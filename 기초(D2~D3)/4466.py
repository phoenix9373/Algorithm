for c in range(1, int(input())+1):
    n, k = map(int, input().split())
    s = sorted(list(map(int, input().split())), reverse=True)
    r = sum(s[0:k])
    print(f'#{c} {r}')