def check(row, col):
    for i in range(row):
        if row - i == abs(col - sel[i]):
            return True # 대각선에 걸림.
    return False # 대각선에 걸리지 않음.

def back(row):
    global cnt
    if row == n:
        cnt += 1
        return

    for col in range(n):
        if visited_col[col]:
            continue
        if check(row, col):
            continue
        sel[row] = col # row idx에 col 번호를 저장.
        visited_col[col] = 1 # 방문한 열을 표시.
        back(row + 1)
        visited_col[col] = 0


n = int(input())
sel = [0] * n
visited_col = [0] * n # columns 전체.
cnt = 0
back(0)
print(cnt)