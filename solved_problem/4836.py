import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    # List 2를 이용해서 풀어보자.
    n = int(input())

    # 격자무늬 생성.
    arr = [['' for _ in range(10)] for _ in range(10)]

    for _ in range(n):
        x_1, y_1, x_2, y_2, c = map(int, input().split())
     
        for x in range(x_1, x_2 + 1):
            for y in range(y_1, y_2 + 1):
                if c == 1:
                    arr[x][y] += 'r'
                else:
                    arr[x][y] += 'b'
    
    cnt = 0
    for row in arr:
        for col in row:
            if (col == 'rb') or (col =='br'):
                cnt += 1
    print(f'#{test_case} {cnt}')



    # ///////////////////////////////////////////////////////////////////////////////////
