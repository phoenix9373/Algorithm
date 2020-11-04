import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
res = [0] * N

for i, idx in zip(range(1, N + 1), nums):
    if res[idx] == 0:
        res[idx] = i
    else:
        while res[idx] != 0:
            i, res[idx] = res[idx], i
            idx += 1
            if res[idx] == 0:
                res[idx] = i
                break
res = res[::-1]
print(*res)