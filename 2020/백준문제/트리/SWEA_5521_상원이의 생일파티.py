for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    adj_list = [[] for _ in range(N + 1)]
    for _ in range(M):
        s, e = map(int, input().split())
        adj_list[s].append(e)
        adj_list[e].append(s)
    friends = set()
    for w in adj_list[1]:
        friends.add(w)
        for w2 in adj_list[w]:
            friends.add(w2)
    cnt = len(friends) - 1 if 1 in friends else len(friends)

    print('#{} {}'.format(tc, cnt))
# 1
# 3 2
# 1 2
# 3 2