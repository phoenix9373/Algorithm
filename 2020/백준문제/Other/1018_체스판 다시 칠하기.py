n, m = map(int, input().split()) # m*n
arr = [list(input()) for i in range(n)]
# 왼쪽 맨 위가 W일때, B일때를 나누어 구함.
# 최대 row = (n - 8) index까지 가능.
max_r = n - 8 # 2
max_c = m - 8
s = ['W', 'B']
count = []
for char in s:
    for r in range(0, max_r + 1):
        for c in range(0, max_c + 1):
            test = [row[c:c+8] for row in arr[r:r+8]]
            cnt = 0
            for i in range(8):
                for j in range(8):
                    if r % 2 == c % 2:
                        if i % 2 == j % 2 and test[i][j] != char:
                            cnt += 1
                        elif i % 2 != j % 2 and test[i][j] == char:
                            cnt += 1
                    elif r % 2 != c % 2:
                        if i % 2 == j % 2 and test[i][j] == char:
                            cnt += 1
                        elif i % 2 != j % 2 and test[i][j] != char:
                            cnt += 1
            count.append(cnt)
print(min(count))