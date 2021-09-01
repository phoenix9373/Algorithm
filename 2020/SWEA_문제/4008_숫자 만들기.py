import sys
sys.stdin = open('input.txt', 'r')


# 같은 깊이에서 같은 값을 사용하는 것만 줄이자.
def perm(idx):
    if idx == N - 1:
        cases.append(''.join(map(str, sel)))
        return

    tmp = -1
    for i in range(N - 1):
        if visited[i] == 0 and tmp != operations[i]:
            visited[i] = 1
            sel[idx] = operations[i]
            tmp = operations[i]
            perm(idx + 1)
            visited[i] = 0


for tc in range(1, int(input()) + 1):
    N = int(input())
    operation = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    operations = [] # 연산자 개수.

    for i in range(4):
        for j in range(operation[i]):
            operations.append(i + 1)

    visited = [0] * (N - 1)
    sel = [0] * (N - 1)
    cases = []
    perm(0)


    max_val = -pow(2, 30)
    min_val = pow(2, 30)
    for case in cases:
        ans = nums[0]

        for i in range(N - 1):
            if case[i] == '1':
                ans += nums[i + 1]
            elif case[i] == '2':
                ans -= nums[i + 1]
            elif case[i] == '3':
                ans = ans * nums[i + 1]
            else:
                ans = int(ans / nums[i + 1])

        if ans > max_val:
            max_val = ans
        if ans < min_val:
            min_val = ans

    print('#{} {}'.format(tc, max_val - min_val))

# 1
# 6
# 1 4 0 0
# 1 2 3 4 5 6