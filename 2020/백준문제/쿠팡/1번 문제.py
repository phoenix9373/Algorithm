def sol(k, N):
    res = ''
    i = 1
    M = k
    # 최댓값 찾기.
    while N > M:
        i += 1
        M = pow(k, i)

    while N:
        i -= 1
        tmp = N // pow(k, i)
        if tmp != 0:
            res += str(tmp)
        N = N % pow(k, i)

    ans = 1
    for i in res:
        ans = ans * int(i)

    return [k, ans]


def solution(n):

    result = []
    for i in range(2, 9):
        result.append(sol(i, n))
    result = sorted(result, key=lambda x: (-x[1], -x[0]))
    ans = result[0]
    return ans


print(solution(100))