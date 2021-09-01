def solution(old_arr):
    l = len(old_arr)
    new_arr = [[0] * l for _ in range(l)]

    c_s, c_l = 0, l - 1
    r_s, r_l = 0, l - 1

    if l % 2 == 1:
        new_arr[l//2][l//2] = old_arr[l//2][l//2]

    while c_s < c_l and r_s < r_l:
        length = c_l - c_s + 1
        for i in range(length):
            new_arr[r_s + i][c_l] = old_arr[r_s][c_s + i]
        for i in range(length):
            new_arr[r_l][c_l - i] = old_arr[r_s + i][c_l]
        for i in range(length):
            new_arr[r_l - i][c_s] = old_arr[r_l][c_l - i]
        for i in range(length):
            new_arr[r_s][c_s + i] = old_arr[r_l - i][c_s]
        c_s += 1
        r_s += 1
        c_l -= 1
        r_l -= 1
    return new_arr


for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    res1 = solution(arr)
    res2 = solution(res1)
    res3 = solution(res2)

    print('#{}'.format(tc))
    for k in range(N):
        for res in [res1, res2, res3]:
            print(*res[k], end=' ', sep='')
        print()