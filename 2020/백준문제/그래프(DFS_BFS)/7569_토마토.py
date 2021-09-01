from collections import deque

dl = [1, -1, 0, 0, 0, 0] # 위, 아래
di = [0, 0, 1, -1, 0, 0] # 앞, 뒤
dj = [0, 0, 0, 0, 1, -1] # 좌, 우


def bfs(qu, count):
    # 0 check

    while qu:
        # 큐가 한 번씩 실행될 때마다 count += 1
        count += 1
        # 한번의 큐 실행 동안 모든 큐를 다 뽑아서 이동시킨다.
        for _ in range(len(qu)):
            i, j, l = qu.popleft()

            for k in range(6):
                ni = i + di[k]
                nj = j + dj[k]
                nl = l + dl[k]
                # 1. index 조건에 안 맞으면 다음으로.
                if not (0 <= ni < N and 0 <= nj < M and 0 <= nl < H):
                    continue
                # 2. 다음 갈 곳이 0이 아니면 패스.
                if not (arr[nl][ni][nj] == 0):
                    continue
                # 모든 조건에 맞으면 큐에 추가하고, arr 값 갱신
                q.append([ni, nj, nl])
                arr[nl][ni][nj] = arr[l][i][j] + 1
    return count


# 모두 익지 못하는 상황 체크
def check(result, tomato):
    for l in range(H):
        for i in range(N):
            if 0 in tomato[l][i]:
                return -1
    return result


# M 가로(j), N 세로(i), H 높이(l)
M, N, H = map(int, input().split())

arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

# 1인 지점 모아서 bfs에 전달.
q = deque()

for j in range(M):
    for i in range(N):
        for l in range(H):
            if arr[l][i][j] == 1:
                q.append([i, j, l])

res = bfs(q, -1)
final_res = check(res, arr)
print(final_res)