# 필요한 방의 최소 개수 찾기
# 같은 학년, 남남, 여여, 한 명만 배정 가능.
N, K = map(int, input().split()) # 1~1000, 2~1000
# 여: 0, 남:1, 학년: 1~6
boy = [0 for _ in range(7)]
girl = [0 for _ in range(7)]

for _ in range(N):
    sex, grade = map(int, input().split())
    if sex == 1:
        boy[grade] += 1
    else:
        girl[grade] += 1


def plus(arr, k):
    res = 0
    for i in arr:
        if i: # 값이 있으면
            q, r = divmod(i, k)
            if r:
                res += q + 1
            else:
                res += q
    return res


ans = plus(boy, K) + plus(girl, K)
print(ans)