# import sys
# sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    # 최대는 a+b / 모두 구독하는 사람.
    # 최소는 max(a,b) - min(a,b)
    n, a, b = map(int, input().split())
    if a+b <= n:
        M = min(a, b)
        N = 0
    else:
        M = min(a, b)
        N = a+b-n
    print(f'#{test_case} {M} {N}')