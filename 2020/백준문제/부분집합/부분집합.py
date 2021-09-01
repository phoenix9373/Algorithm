# 부분집합

arr = [1, 2, 3, 4, 5]
n = len(arr)
cnt = 0

for i in range(1 << n): # 총 2^n 개의 부분집합이 있으므로, 반복 시행
    cnt += 1
    for j in range(n): # 각 부분집합마다 비트연산으로 원소 포함 유무를 결정하기 위해 n번 반복시행
        if i & (1<<j):
            print(arr[j], end=' ')
    print()

print('총 부분집합 개수: ', cnt)