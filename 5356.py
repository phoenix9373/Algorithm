import sys
sys.stdin = open('input.txt', 'r')
for c in range(1, int(input())+1):
    t = [' '.join(input()).split() for _ in range(5)]
    m = max(list(map(len, t)))
    for i in range(len(t)):
        if len(t[i]) < m:
            t[i] = t[i] + [0]*(m-len(t[i]))
    text = ''
    for j in range(m):
        for i in range(len(t)):
            if t[i][j] != 0:
                text += t[i][j]
    print(f'#{c} {text}')