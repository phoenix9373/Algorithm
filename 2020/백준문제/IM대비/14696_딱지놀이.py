# 별4 > 동그라미3 > 네모2 > 세모1 / 무승부
# 무승부: D

N = int(input()) # 1~1000
for _ in range(N):
    a = list(map(int, input().split()))[1:]
    b = list(map(int, input().split()))[1:]

    for i in range(4, 0, -1):
        a_cnt = a.count(i)
        b_cnt = b.count(i)
        if a_cnt > b_cnt:
            print('A')
            break
        elif b_cnt > a_cnt:
            print('B')
            break
    else:
        print('D')