# N은 짝수, 두 팀으로 나눔.
# 팀 나누는 방법은 조합?
def comb(idx, sidx):
    if sidx == N // 2:
        global teams
        teams.append(sel.copy())
        return

    for i in range(idx, N):
        sel[sidx] = i
        comb(i + 1, sidx + 1)


N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]
teams = []
sel = [0] * (N // 2)
comb(0, 0)
M = pow(10, 7)

for i in range(len(teams)):
    t1 = teams[i]
    t2 = [j for j in range(N) if j not in t1]

    s1 = sum([info[x][y] for x in t1 for y in t1])
    s2 = sum([info[x][y] for x in t2 for y in t2])
    tmp = abs(s1 - s2)
    if M > tmp:
        M = tmp

print(M)