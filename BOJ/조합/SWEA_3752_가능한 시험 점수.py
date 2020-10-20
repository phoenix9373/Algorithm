for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    nums = [0] * (sum(arr) + 1)
    nums[0] = 1
    for i in arr[::-1]:
        for j in range(sum(arr), -1, -1):
            if nums[j] == 1:
                nums[i+j] = 1
    print('#{} {}'.format(tc, nums.count(1)))