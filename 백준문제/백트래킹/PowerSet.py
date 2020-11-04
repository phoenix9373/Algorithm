# Powerset: 어떤 집합의 공집합과 자기자신을 포함한 모든 부분집합.
#
arr = [1, 2, 3]
n = len(arr)

# # 비트 연산으로 구하기
# for j in range(1<<n): # 부분집합 개수.
#     for i in range(n): # 각 원소 포함 여부.
#         if j & (1<<i):
#             print(arr[i], end=' ')
#     print()

# ------------------------------------------------------------------------------------------

# 백트래킹으로 구하기.
arr = [1, 2, 3]
N = len(arr)
sel = [0] * N


def powerset(idx):
    if idx == N:
        print(sel, " : ", end=" ")
        for i in range(N):
            if sel[i]:
                print(arr[i], end=' ')
        print()
        return

    # 해당자리를 뽑고 가고
    sel[idx] = 1
    powerset(idx + 1)
    sel[idx] = 0
    powerset(idx + 1)

powerset(0)