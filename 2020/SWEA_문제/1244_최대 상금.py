import sys
sys.stdin = open('input.txt', 'r')


def solution(arr, k):
    global ans
    if k == c:
        return

    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if i == j:
                continue
            arr[i], arr[j] = arr[j], arr[i]
            tmp = ''.join(arr)
            if (tmp, k) not in ans:
                ans.append((tmp, k))
            else:
                arr[j], arr[i] = arr[i], arr[j]
                continue
            solution(arr, k + 1)
            arr[j], arr[i] = arr[i], arr[j]


for tc in range(1, int(input()) + 1):
    nums, c = input().split()
    nums = list(nums)
    c = int(c)
    ans = []
    solution(nums, 0)
    print('#{} {}'.format(tc, max(ans)[0]))

# 10
# 123 1
# 2737 1
# 757148 1
# 78466 2
# 32888 2
# 777770 5
# 436659 2
# 431159 7
# 112233 3
# 456789 10