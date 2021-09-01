nums = []
i = 1
cnt = int(input())
while len(nums) < cnt:
    if '666' in str(i):
        nums.append(i)
    i += 1

print(nums[-1])