import sys
sys.stdin = open('input.txt', 'r')

def dfs(v):
    global result

    result.append(v)
    to_visit[v] -= 1

    for w in adj[v]:
        if to_visit[w] == 1:
            dfs(w)
        elif to_visit[w] > 1:
            to_visit[w] -= 1


for tc in range(1, 11):
    V, E = map(int, input().split())
    nums = list(map(int, input().split()))
    adj = [[] for _ in range(V + 1)]
    to_visit = [0] * (V + 1)

    for i in range(E):
        s, e = nums[i*2], nums[i*2 + 1]
        to_visit[e] += 1
        adj[s].append(e)

    start_point = [idx for idx, i in enumerate(to_visit) if (idx != 0 and i == 0)]
    result = []

    for i in start_point:
        dfs(i)
    print('#{} '.format(tc), end='')
    print(*result)