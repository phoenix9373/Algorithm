import sys
n = int(sys.stdin.readline())
info = []
for i in range(n):
    person = sys.stdin.readline().split()
    info.append([int(person[0]), person[1], i])
info = sorted(info, key=lambda x: (x[0], x[2]))
for k in info:
    print(k[0], k[1])