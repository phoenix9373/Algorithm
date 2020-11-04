# 10개 중 9개 틀림.

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    dic = {k: [] for k in range(N + 1) if k != 0}
    for i in range(0, len(nums), 2):
        s, e = nums[i], nums[i + 1]
        if s not in dic[e]:
            dic[s].append(e)

    ans = N
    for k in dic.keys():
        ans -= len(dic[k])

    print('#{} {}'.format(tc, ans))

# 예외
# 1
# 4 3
# 1 2 3 4 4 3
