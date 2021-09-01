for tc in range(1, int(input())+1):
    n = int(input())
    num = [int(input()) for _ in range(n)]
    m = sum(num)/n
    k = sum(list(map(lambda x: abs(x-m), num))) / 2
    print(f'#{tc} {int(k)}')