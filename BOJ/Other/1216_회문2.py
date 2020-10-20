import sys
sys.stdin = open('input.txt', 'r')

def find(s):
    M = 0
    for i in range(100, 1, -1): # 회문 길이
        if M > i:
            break
        for k in range(100):
            for j in range(100 - i + 1): # 컬럼.
                test = s[k][j:j+i]
                if test == test[::-1] and i > M:
                    M = i
                    break
    return M

def ch(arr):
    for x in range(100):
        for y in range(100):
            if x > y:
                arr[x][y], arr[y][x] = arr[y][x], arr[x][y]
    return arr

for t in range(1, 11):
    n = int(input())
    grid = [list(input()) for i in range(100)]
    a = find(grid)
    b= find(ch(grid))

    if a > b:
        print('#{} {}'.format(t, a))
    else:
        print('#{} {}'.format(t, b))