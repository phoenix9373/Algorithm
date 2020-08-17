import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n, m = map(int, input().split())

    nums = list(map(int, input().split()))

    # 처음 값으로 초기화.
    min_sum = sum(nums[0:m])
    max_sum = sum(nums[0:m])

    for i in range(n - m + 1):
        num_sum = sum(nums[i:i+m])
        
        # 구간 최대합.
        if num_sum > max_sum:
            max_sum = num_sum
        
        # 구간 최소합.
        if num_sum < min_sum:
            min_sum = num_sum

    result = max_sum - min_sum

    print(f'#{test_case} {result}')
    # ///////////////////////////////////////////////////////////////////////////////////
