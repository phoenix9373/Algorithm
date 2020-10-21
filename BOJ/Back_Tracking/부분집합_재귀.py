arr = [1, 2, 3] # set
N = len(arr)
A = [0] * N


def powerset(n, k, cursum): # n: 원소의 갯수, k: 현재 depth
    if cursum > 10: return # 백트래킹.
    if n == k:
        print(A, end=': ')
        for i in range(n):
            if A[i]:
                print(arr[i], end= " ")
        print()
    else:
        A[k] = 1           # k번 요소 포함.
        powerset(n, k + 1, cursum + arr[k]) # 다음 요소 포함 여부 결정.
        A[k] = 0           # k번 요소 미포함.
        powerset(n, k + 1) # 다음 요소 포함 여부 결정.

powerset(N, 0)