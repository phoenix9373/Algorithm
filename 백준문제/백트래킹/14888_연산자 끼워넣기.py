N = int(input())
nums = list(map(int, input().split()))
module = list(map(int, input().split()))
Max = -float('inf')
Min = float('inf')


def sol(v, mod, cumsum):


    if v == len(nums):
        global Max, Min
        if cumsum > Max:
            Max = cumsum
        if cumsum < Min:
            Min = cumsum
        return

    for i in range(4):
        if mod[i] != 0:
            mod[i] -= 1
            if i == 0:
                sol(v + 1, mod, cumsum + nums[v])
            elif i == 1:
                sol(v + 1, mod, cumsum - nums[v])
            elif i == 2:
                sol(v + 1, mod, cumsum * nums[v])
            elif i == 3:
                tmp = -((-cumsum) // nums[v]) if cumsum < 0 and nums[v] > 0 else cumsum//nums[v]
                sol(v + 1, mod, tmp)
            mod[i] += 1


sol(1, module, nums[0])
print(Max)
print(Min)


# 반례...?
# 3
# 1 10 2
# 0 1 0 1
