# 정렬 종류
# 버블 정렬, 카운팅 정렬, 선택 정렬, 퀵 정렬, 삽입 정렬, 병합 정렬
# 버블 또는 카운팅으로 해보기.

# 1. 버블
# 처음의 위치에 대해 나머지 값과 비교하며 가장 작은 값 할당.
# 그 다음 값의 위치에 그 다음으로 작은 값 할당. 반복.

# nums는 1000 이하 정수.
n = int(input())
nums = [int(input()) for _ in range(n)]

for i in range(n):
    for j in range(i+1, n):
        if nums[i] > nums[j]:
            nums[i], nums[j] = nums[j], nums[i]

print(*nums, sep='\n')

# 2. 선택 정렬: 버블 정렬과 유사, but 교환 횟수가 적음.
# 버블 정렬이 최솟값을 찾을때 교환을 비교마다 하는 반면
# 선택 정렬은 최솟값의 index를 찾아서 해당 index와 1번 바꿈.

for i in range(n-1):
    min_idx = i
    for j in range(i+1, n):
        if nums[min_idx] > nums[j]:
            min_idx = j
    nums[i], nums[min_idx] = nums[min_idx], nums[i]

print(nums)