def choice(row, prob=1):
    global max_prob

    if row == n:
        if prob > max_prob:
            max_prob = prob
        return

    if prob <= max_prob: # max보다 작을 경우, 백트래킹
        return

    for i in range(n): # 총 n번 반복. n은 직원 수와 할 일.
        if visited_col[i] == 0:
            visited_col[i] = 1
            choice(row + 1, prob*(arr[row][i] / 100))
            visited_col[i] = 0

for tc in range(1, int(input()) + 1):
    n = int(input())

    arr = [list(map(int, input().split())) for _ in range(n)]
    visited_col = [0] * n
    max_prob = pow(10, -31)
    choice(0)
    # print('#{} {:0<9}'.format(tc, round(max_prob*100, 6)))
    print(f'#{tc} {max_prob*100:.6f}')
