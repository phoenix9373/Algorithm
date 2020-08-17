import sys
import time
sys.stdin = open("input.txt", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    case = int(input())

    nums = [list(map(int, input().split())) for _ in range(100)]
    max_num = 0
    left = 0
    right = 0
    for i in range(100):
        s_1 = sum(nums[i])
        s_2 = 0
        for j in range(100):
            s_2 += nums[j][i]
            if i == j:
                left += nums[i][j]
            if i + j == 99:
                right += nums[99-i][j]
        if max_num < max(s_1, s_2):
            max_num = max(s_1, s_2)
    result = max(max_num, right, left)

    print(f'#{test_case} {result}')

    # ///////////////////////////////////////////////////////////////////////////////////
