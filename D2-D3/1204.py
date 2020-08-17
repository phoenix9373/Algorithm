# import sys
# sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())

    nums = list(map(int, input().split()))
    k = [0 for _ in range(101)]
    for i in nums:
        k[i] += 1
    for j in range(100, -1, -1):
        if k[j] == max(k):
            print(f'#{test_case} {j}')