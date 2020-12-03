N, B = map(int, input().split())
arr = [list(map(lambda x: int(x) % 1000, input().split())) for _ in range(N)]
matrix_dict = {}


def sol(matrix, b):
    if b == 1:
        return matrix

    if b // 2 not in matrix_dict.keys():
        matrix_dict[b // 2] = mul_matrix(sol(matrix, b // 2), sol(matrix, b // 2))

    if b % 2 == 1:
        # 위에서 들어온 matrix의 b // 2 제곱 * matrix
        return mul_matrix(matrix_dict[b // 2], matrix)
    else:
        # 위에서 들어온 matrix의 b // 2 제곱 2개
        return matrix_dict[b // 2]


def mul_matrix(u, v):
    tmp_list = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            tmp = 0
            for k in range(N):
                tmp += u[i][k] * v[k][j]
            tmp_list[i][j] = tmp % 1000
    return tmp_list


ans = sol(arr, B)
for row in ans:
    print(*row)
