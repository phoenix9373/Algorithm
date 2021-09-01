N = int(input())
nums = sorted(list(map(int, input().split())))
for i in range(N - 1):
    nums[i + 1] += nums[i]

print(sum(nums))