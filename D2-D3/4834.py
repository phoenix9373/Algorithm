import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n = int(input())

    nums = list(map(int, ' '.join(input()).split()))

    counts = [0]*10
    
    for num in nums:
        counts[num] += 1
    
    max_num = 0
    final_idx = 0
    for idx, i in enumerate(counts):
        if i >= max_num:
            max_num = i
            final_idx = idx

    print(f'#{test_case} {final_idx} {max_num}')

    # ///////////////////////////////////////////////////////////////////////////////////
