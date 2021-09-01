import sys

n = int(sys.stdin.readline())
nums = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
nums = sorted(nums, key=lambda x: (x[0], x[1]))
for k in nums:
    print(k[0], k[1])