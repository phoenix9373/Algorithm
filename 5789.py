# N개 상자, 0으로 적힘
# Q회 동안 일정 범위의 연속한 상자를 동일한 숫자로 변경
# i번째 작업(1<=i<=Q)에 대해 L ~ R까지 i로 변경.
# N개의 상자에 적힌 번호를 순서대로 출력

for c in range(1, int(input()) + 1):
    n, q = map(int, input().split())
    N = [0]*n
    for i in range(1, q+1):
        l, r = map(int, input().split())
        for j in range(l-1, r):
            N[j] = i
    print(f'#{c}', *N)