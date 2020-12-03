def find_max():
    # global N, M, board, houses
    max_val = -1
    ideal_plus = len(houses) * M  # 최대 방범 가능한 집의 개수 * 개당 비용
    MAX_K = 1
    while MAX_K ** 2 + (MAX_K - 1) ** 2 <= ideal_plus:  # 최대 K 값을 찾는다.
        MAX_K += 1
    MAX_K -= 1
    if MAX_K == 0:  # 하나뿐이면 0을 return
        return 0
    for cur_K in range(1, MAX_K + 1):  # 각각의 K에 따라
        minus = cur_K ** 2 + (cur_K - 1) ** 2  # cost
        for r in range(N):
            for c in range(N):  # 모든 좌표에 대해 실행.
                in_cnt = 0  # 포함되는 home의 개수.
                for house in houses:
                    hr, hc = house
                    if abs(hr - r) + abs(hc - c) < cur_K: # 거리를 계산해주고, 안쪽에 있으면 카운트 + 1
                        in_cnt += 1
                if in_cnt * M - minus >= 0:  # 조건을 만족하고, 최댓값보다 크면 갱신해준다.
                    max_val = max(in_cnt, max_val)

    return max_val


if __name__ == "__main__":
    # sys.stdin = open('sample_input.txt', 'r')
    T = int(input())
    for t in range(1, T + 1):
        N, M = list(map(int, input().split()))
        board = []
        board = [list(map(int, input().split())) for _ in range(N)]
        houses = []
        for r in range(N):
            for c in range(N):
                if board[r][c] == 1:
                    houses.append((r, c))  # 집들의 좌표를 추가.
        max_cnt = find_max()
        print('#{}'.format(t), max_cnt)