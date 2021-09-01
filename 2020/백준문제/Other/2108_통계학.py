import sys

n = int(sys.stdin.readline())
nums = sorted([int(sys.stdin.readline()) for _ in range(n)])
print(round(sum(nums)/n))
print(nums[n//2])

k = -min(nums)
m = max(nums)
count = [0] * (m+k+1)
for i in range(n):
    count[nums[i]+k] += 1
most_freq = [idx - k for idx, j in enumerate(count) if j == max(count)]
if len(most_freq) > 1:
    print(most_freq[1])
else:
    print(most_freq[0])
print(max(nums) - min(nums))