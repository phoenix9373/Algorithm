from collections import deque

q = deque()
N = int(input())
for i in range(1, N + 1):
    q.append(i)

while len(q) > 1:
    q.popleft()
    if len(q) == 1:
        print(q[0])
        break
    s = q.popleft()
    q.append(s)

if N == 1:
    print(1)