import sys
sys.stdin = open("test.txt", "r")
for case in range(1, int(input()) + 1):
    n = int(input())
    nums = [[1 if i else 0 for i in list(map(int, input().split()))] for _ in range(n)]
    result = []
    ignore = []
    for i in range(n):
        for j in range(n):
            r, c = 0, 0
            if (nums[i][j]==1) and ((i,j) not in ignore):
                while (i+r <= n-1) and (nums[i+r][j]==1):
                    r += 1
                while (j+c <= n-1) and (nums[i][j+c]==1):
                    c += 1
                for x in range(i, i+r):
                    for y in range(j, j+c):
                        ignore.append((x, y))
                # print('i:', i, 'j:', j)
                result.append([r, c])
    s = sorted([(i, j[0]*j[1]) for i, j in enumerate(result)], key=lambda x: x[1])
    u = [0]*len(result)
    for idx, (i, j) in enumerate(s):
        u[idx] = result[i]
    for i in range(len(u)):
        for j in range(i+1, len(u)):
            a = u[i][0]*u[i][1]
            b = u[j][0]*u[j][1]
            if (a == b) and (u[i][0] > u[j][0]):
                u[i], u[j] = u[j], u[i] 

    f = [j for i in u for j in i]
    print(f'#{case}', len(result), *f)

