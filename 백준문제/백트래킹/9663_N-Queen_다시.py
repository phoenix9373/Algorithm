N = int(input())
col_visit = [-1] * N

total_cnt = 0

def check(row, col):
    for j in range(row):
        if row - j == abs(col - col_visit[j]):
            return True # 대각선.
    return False

def queen(row):

    if row == N:
        global total_cnt
        total_cnt += 1
        return

    for i in range(N):
        if col_visit[i] != -1:
            continue
        if check(row, i):
            continue
        col_visit[i] = i # 자기 자신의 col_idx를 저장.
        queen(row + 1)
        col_visit[i] = -1 # 다른 것 선택할 수 있으니까.
queen(0)
print(total_cnt)