for d in range(1, int(input())+1):
    a, b, c = map(int, input().split())
    print(f'#{d} {c//min(a,b)}')