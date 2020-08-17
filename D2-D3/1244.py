# import sys
# sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    nums, c = input().split()
    nums = list(map(int, ' '.join(nums).split()))
    c = int(c)