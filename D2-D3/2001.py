import sys

sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    # print(f'#{test_case} start')
    n, m = map(int, input().split())
    # print(f'{test_case} middle')
    
    nums = [list(map(int, input().split())) for i in range(n)]
    
    # m의 값만큼 m x m을 탐색.
    # 각각의 값을 탐색하면서 최댓값을 산출.
    # 이전 값보다 크면 갱신.
    # n=5, m=2 일 때 총 16번 반복
    
    # n=5, m=3 일 때 총 9번 반복.

    max_num = 0
    for i in range(0, n-m+1):
        for j in range(0, n-m+1):
            num_sum = sum([sum(k[j:j+m]) for k in nums[i:i+m]])
            if num_sum > max_num:
                max_num = num_sum
    
    print(f'#{test_case} {max_num}')

    
    # ///////////////////////////////////////////////////////////////////////////////////