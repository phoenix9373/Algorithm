from collections import deque
res = 0

def BFS(v, visit, adj):

    q = deque()
    q.append(v)
    visit[v] = 1

    while q:
        t = q.popleft()
        print(t, end=' ')
        for w in adj[t]:
            if visit[w] == 0:
                q.append(w)
                visit[w] = visit[v] + 1
    print(visit)


def check(dep, adj, h, d, num):
    if num == 2:
        global a
        a += 1

    for w in adj[dep]:
        if w in [h, d]:
            num += 1
        check(w, adj, h, d, num)


def solution(depar, hub, dest, roads):
    global a

    adj_list = {dest: []}
    for s, e in roads:
        if s in adj_list.keys():
            adj_list[s].append(e)
        else:
            adj_list[s] = [e]

    # visited = {dest: 0}
    # for k in adj_list.keys():
    #     visited[k] = 0
    res = 0
    check(depar, adj_list, hub, dest, res)

    ans = a
    return ans

a = 0

print(solution("SEOUL", "DAEGU", "YEOSU", [["ULSAN","BUSAN"],["DAEJEON","ULSAN"],["DAEJEON","GWANGJU"],["SEOUL","DAEJEON"],["SEOUL","ULSAN"],["DAEJEON","DAEGU"],["GWANGJU","BUSAN"],["DAEGU","GWANGJU"],["DAEGU","BUSAN"],["ULSAN","DAEGU"],["GWANGJU","YEOSU"],["BUSAN","YEOSU"]]))
# print(solution("ULSAN", "SEOUL", "BUSAN", [["SEOUL","DAEJEON"],["ULSAN","BUSAN"],["DAEJEON","ULSAN"],["DAEJEON","GWANGJU"],["SEOUL","ULSAN"],["DAEJEON","BUSAN"],["GWANGJU","BUSAN"]]))


