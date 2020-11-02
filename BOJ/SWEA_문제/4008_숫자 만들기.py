# import sys
# sys.stdin = open('input.txt', 'r')


for tc in range(1, int(input()) + 1):
    N = int(input())
    oper = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    operations = []

    for i in range(4):
        for j in range(oper[i]):
            operations.append(i + 1)
    cases = []

    max_val = 0
    min_val = pow(2, 30)
    for case in cases:
        ans = nums[0]
        for i in range(N - 1):
            if case[i] == 1:
                ans += nums[i + 1]
            elif case[i] == 2:
                ans -= nums[i + 1]
            elif case[i] == 3:
                ans = ans * nums[i + 1]
            else:
                ans = int(ans / nums[i + 1])
        if ans > max_val:
            max_val = ans
        if ans < min_val:
            min_val = ans
    print('#{} {}'.format(tc, max_val - min_val))