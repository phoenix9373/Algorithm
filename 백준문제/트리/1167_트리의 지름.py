# 출처: https://developmentdiary.tistory.com/436

import sys

V = int(sys.stdin.readline().strip())

matrix = [[] for _ in range(V + 1)]

# 입력
for _ in range(V):
    path = list(map(int, sys.stdin.readline().split()))
    path_len = len(path)
    for i in range(1, path_len // 2):
        matrix[path[0]].append([path[i * 2 - 1], path[i * 2]])

# 1번째 dfs 결과
result_1 = [0 for _ in range(V + 1)]


def dfs(s, mat, res):
    for e, d in matrix[s]:
        if res[e] == 0:
            res[e] = res[s] + d
            dfs(e, mat, res)

dfs(1, matrix, result_1)
result_1[1] = 0

tmp_max = 0 # 최댓값 구하기
index = 0 # 최장 경로 노드

for i in range(len(result_1)):
    if tmp_max < result_1[i]:
        tmp_max = result_1[i]
        index = i

# 어쨋든 루트에서 좌우로 가장 큰 값을 찾으면 되는거니까.
# 어떤 점에서든 상관없이 dfs가 큰 것 2번을 연속으로 큰 값을 구하면 자동으로 지름이 구해진다.
# 최장 경로 노드에서 다시 dfs를 통해 트리 지름 구하기.
result = [0 for _ in range(V + 1)]
dfs(index, matrix, result)
result[index] = 0
print(max(result))