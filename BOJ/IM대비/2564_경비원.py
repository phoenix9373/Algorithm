# 왼쪽 위 점을 기준으로 한 쪽방향으로 돌았을 때,
# 각각의 점에 대해 거리를 구한다.

C, R = map(int, input().split())
round = 2*C + 2*R
N = int(input())

def distance(i, d):
    tmp = [0, d, 2*C + R - d, round - d, C + d]
    return tmp[i]

ans = 0

dist = []
for _ in range(N + 1):
    idx, pos = map(int, input().split())
    dist.append(distance(idx, pos))
my_dist = dist[-1]

for i in range(N):
    cand = abs(my_dist - dist[i])
    ans += min(cand, round - cand)
print(ans)