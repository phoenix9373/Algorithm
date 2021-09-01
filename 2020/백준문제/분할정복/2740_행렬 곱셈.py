# N*M 행렬
# M*K 행렬
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
M, K = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(M)]
C = [[0] * K for _ in range(N)]

for i in range(N):
    for j in range(K):
        tmp = 0
        for m in range(M):
            tmp += A[i][m] * B[m][j]
        C[i][j] = tmp


for row in C:
    print(*row)