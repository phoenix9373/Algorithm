import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    # 부분 집합의 합. 
    n, k = map(int, input().split())
    cnt = 0
    arr = [i for i in range(1, 13)]

    for i in range(1<<12):
        num_sum = []
        for j in range(12):
            if i&(1<<j):
                num_sum.append(arr[j])
        if (len(num_sum) == n) and sum(num_sum) == k:
            cnt += 1

    print(f'#{test_case} {cnt}')


    # ///////////////////////////////////////////////////////////////////////////////////
