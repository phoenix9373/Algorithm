import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    V, E = map(int, input().split())
    info = list(map(int, input().split()))
    link = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)
    order = []

    for i in range(E):
        link[info[2 * i + 1]].append(info[2 * i]) # 반대로 입력한 이유는??

    while visited.count(1) != V:
        for i in range(1, V + 1):
            if visited[i] == 1:
                continue
            for j in link[i]: # for-else 구문에서 for문의 link[i]가 None 이므로 else로 바로 넘어간다.
                if visited[j] == 0:
                    break
            else:
                order.append(i)
                visited[i] = 1
    print(f'#{tc}', *order)