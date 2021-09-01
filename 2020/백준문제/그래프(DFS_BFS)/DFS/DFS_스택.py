# 7 8
# 1 2
# 1 3
# 2 4
# 2 5
# 4 6
# 5 6
# 6 7
# 3 7


V, E = map(int, input().split())

# 데이터 준비: 인접행렬, 인접 리스트, 간선 리스트 등.
# 한 칸 더 크게 만드는 이유 -> 인덱스 맞추기
# 0번 인덱스 버리기
arr = [[0] * (V+1) for _ in range(V+1)]

#
for i in range(E): # E 간선수, V 정점수
    st, ed = map(int, input().split())
    # 무향 그래프이기 때문에 서로 연결되있음을 표시
    arr[st][ed] = arr[ed][st] = 1

# 방문배열
visited = []
# 스택
stack = []
# 시작 정점을 담는다.
stack.append(1)
# 스택이 빌때까지 무한히 반복
while len(stack) > 0:
    v = stack.pop()

    if v not in visited: # 들리지 않은 곳이면, 추가. 시작점도 마찬가지
        print(v, end=" ")
        visited.append(v) # 방문 표시

        for i in range(1, V+1): # 본인을 포함한 모든 정점에 대하여
            if arr[v][i] == 1 and i not in visited: # 만약 i가 인접한 정점이고, 방문하지 않은 곳이면(여기서 자기 자신이 빠짐.)
                stack.append(i) # stack에 추가한다.
