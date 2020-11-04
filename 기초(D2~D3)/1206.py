import sys

sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    # print(f'#{test_case}')
    n = int(input())
    
    arr = list(map(int, input().split())) # 빌딩 높이 값.

    d_x = [-2, -1, 1, 2]
    cnt = 0

    for i in range(2, len(arr) - 2):
        min_diff = 255
        for x in d_x:
            diff = arr[i] - arr[i+x]
            if diff <= 0:
                min_diff = 0
                break
            if min_diff > diff:
                min_diff = diff
        cnt += min_diff
    print(f'#{test_case} {cnt}')
            

    # ///////////////////////////////////////////////////////////////////////////////////
