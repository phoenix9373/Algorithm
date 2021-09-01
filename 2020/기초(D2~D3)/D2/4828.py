import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n = int(input())

    numbers = list(map(int, input().split()))

    # 버블 정렬 이용.
    # n-1, n-2, ..., 1번.
    # 시작: 제일 작은 값 찾기
    # 
    for i in range(n - 1, 0, -1):
        for j in range(0, i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    result = numbers[-1] - numbers[0]
    print(f'#{test_case} {result}')
    # ///////////////////////////////////////////////////////////////////////////////////
