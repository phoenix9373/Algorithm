for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    weights = sorted(list(map(int, input().split())), reverse=True)
    trucks = sorted(list(map(int, input().split())), reverse=True)
    ans = 0

    s = 0
    for t in range(len(trucks)):
        if s == len(weights):
            break
        for w in range(s, len(weights)):
            if trucks[t] >= weights[w]:
                ans += weights[w]
                s = w + 1
                break

    print('#{} {}'.format(tc, ans))