# import sys
# sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    nums = list(map(int, input().split()))
    for i in range(n-1):
        if i % 2:
            for j in range(i+1, n):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        else:
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
    result = ' '.join(map(str, nums[:10]))
    print(f'#{test_case} {result}')