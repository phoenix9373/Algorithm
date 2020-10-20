dy = [-1, 0, -1, 0]
dx = [0, 1, 0, -1]

C, R = map(int, input())
K = int(input())

arr = [[0] * (C + 1) for _ in range(R + 1)]
visited = [[0] * (C + 1) for _ in range(R + 1)]