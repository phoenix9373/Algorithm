# 남 1
# 여 2
def change(x):
    global arr
    if arr[x] == 1:
        arr[x] = 0
    else:
        arr[x] = 1


def boy(num):
    for i in range(num, N + 1, num): # N 까지 포함해야한다.
        change(i)


def girl(num):
    change(num)
    d = 1
    while True:
        l, r = num - d, num + d
        if l > 0 and r <= N and arr[l] == arr[r]: # 스위치 idx 조건.
            change(l)
            change(r)
            d += 1
        else:
            return


N = int(input()) # 스위치 개수
arr = [0] + list(map(int, input().split())) # 스위치 상태
S = int(input()) # 학생 수

for _ in range(S):
    sex, n = map(int, input().split())
    if sex == 1:
        boy(n)
    else:
        girl(n)

for i in range(N // 20 + 1):
    print(*arr[1 + i*20: 1 + (i+1)*20])

'''
30
0 1 0 1 0 0 0 1 1 0 0 1 0 1 0 0 0 1 1 0 0 1 0 1 0 0 0 1 1 0
2
1 3
2 3
'''

'''
0 0 1 1
0 0 0 1
'''
