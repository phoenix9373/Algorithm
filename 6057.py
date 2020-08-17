import sys

sys.stdin = open("test.txt", "r")
for c in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    d = {}
    cnt = 0
    for i in range(1, n+1):
        d[i] = []
    for j in range(m):
        a, b = map(int, input().split())
        d[a].append(b)
        d[b].append(a)
    for i in list(d.keys()):
        if (d.get(i) != None):
            for j in d.get(i):
                if (d.get(j) != None) and (j > i):
                    for k in d.get(j):
                        if (d.get(k) != None) and (k > j):
                            for x in d.get(k):
                                if x == i:
                                    cnt += 1
    print(f'#{c} {cnt}')