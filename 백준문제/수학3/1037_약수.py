M = int(input())
nums = list(map(int, input().split()))
s = max(nums)

while True:
    s += 1
    for i in nums:
        if s % i == 0:
            pass
        else:
            break
    else:
        break

print(s)