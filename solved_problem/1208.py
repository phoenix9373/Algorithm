import sys

sys.stdin = open("input.txt", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n = int(input())
    nums = list(map(int, input().split()))
    cnt = 0

    while cnt < n:
        if max(nums) - min(nums) <= 1:
            break
        cnt += 1
        nums.sort()
        max_idx, min_idx = nums.index(max(nums)), nums.index(min(nums))
        nums[max_idx] -= 1
        nums[min_idx] += 1
        diff = max(nums) - min(nums)
    print(f'#{test_case} {diff}')

    # max index를 찾아서..?!
    # max 값을 찾아서 -1을 하고,
    # min 값을 찾아서 +1을 반복한다.
    # 반복 시에는 count를 세고, 덤프 횟수 n 이내에서 수행한다.
    # count > n이면 종료, 또는 max값과 min 값의 차이가 0 또는 1이면 종료한다.

    # ///////////////////////////////////////////////////////////////////////////////////
