import sys
from collections import deque

N = int(sys.stdin.readline())
q = deque()

for _ in range(N):
    tmp = sys.stdin.readline().split()

    if len(tmp) > 1:
        order = tmp[0]
        num = int(tmp[1])
    else:
        order = tmp[0]

    if order == 'push':
        q.append(num)
    elif order == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            l = q.popleft()
            print(l)
    elif order == 'size':
        print(len(q))
    elif order == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif order == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif order == 'back':
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])