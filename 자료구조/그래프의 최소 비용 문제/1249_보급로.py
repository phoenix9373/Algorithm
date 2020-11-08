import sys
sys.stdin = open('input.txt', 'r')


def dijkstra(arr):
    key = [[float('inf')] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    key[0][0] = 0

    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]

    check = set()
    check.add((0, 0))

    while check:
        # 현재 q에서 가장 작은 D 값을 갖는 인덱스 추출.
        m_i = m_j = 0
        minValue = float('inf')

        for i, j in check:
            if not visited[i][j] and key[i][j] < minValue:
                m_i, m_j = i, j
                minValue = key[i][j]

        # 최소값을 갖는 위치를 확정
        visited[m_i][m_j] = 1
        check.remove((m_i, m_j))

        # 상하좌우 방향에 대해 탐색하고, check에 탐색할 후보를 추가한다.
        for k in range(4):
            ni = m_i + di[k]
            nj = m_j + dj[k]
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                    if key[ni][nj] > key[m_i][m_j] + arr[ni][nj]:
                        key[ni][nj] = key[m_i][m_j] + arr[ni][nj] # 값 갱신.
                        check.add((ni, nj))  # 탐색 후보로 추가.
    return key[N - 1][N - 1]


for tc in range(1, int(input()) + 1):
    N = int(input())
    maps = [list(map(int, ' '.join(input()).split())) for _ in range(N)]
    ans = dijkstra(maps)

    print('#{} {}'.format(tc, ans))