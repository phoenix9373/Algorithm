import sys
# import time


sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    k, n, m = map(int, input().split()) # 차례로 1회 충전시 이동거리, 정류장 개수, 충전기 개수.

    m_list = list(map(int, input().split())) # 충전기 설치 위치.

    cnt = 0
    position = 0
    # x = 0
    while True:
        # x += 1
        # time.sleep(1)
        # print(f'#{x}: {(n-position)}')
        if k >= (n - position): # 이동가능거리 >= (도착위치 - 현재위치)인 경우 종료.
            break
        
        max_move = 0
        for i in m_list:
            if k >= (i - position):
                max_move = (i - position)

        if max_move:
            position += max_move
            cnt += 1
        else:
            cnt = 0
            break
        
    print(f'#{test_case} {cnt}')
    # ///////////////////////////////////////////////////////////////////////////////////
