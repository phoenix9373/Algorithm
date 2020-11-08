# 개수가 짝수이고, 모든 문자의 개수가 짝수일 때.
# 개수가 홀수이고, 한 문자를 제외한 나머지가 짝수일 때.
from collections import Counter

t = input()
n = len(t)


def check(name):
    tmp = Counter(name)
    cnt = 0
    ret, char = '', ''

    for val in tmp.values():
        if val % 2:
            cnt += 1
    if n % 2 == 0 and cnt > 0:
        return ret, char
    if n % 2 == 1 and cnt != 1:
        return ret, char

    for k in tmp:
        if tmp[k] % 2:
            char += k
        else:
            ret += k * (tmp[k] // 2)
    return ret, char


def sol(idx):
    global val
    if not val:
        return

    if idx == len(val):
        t = sel.copy()
        ans.add(''.join(t + [c] + t[::-1]))
        return

    tmp = 0
    for i in range(idx, len(val)):
        if tmp != val[i] and not visited[i]:
            tmp = val[i]
            visited[i] = 1
            sel[idx] = val[i]
            sol(idx + 1)
            visited[i] = 0


val, c = check(t)
visited = [0] * len(val)
sel = [''] * len(val)
ans = set()
sol(0)
if ans:
    print(*sorted(ans))
else:
    print("I'm Sorry Hansoo")