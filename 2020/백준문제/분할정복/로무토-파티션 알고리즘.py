def partition(A, l, r):
    x = A[r]
    i = l - 1
    for j in range(l, r):  # i는 x보다 작은 마지막 인덱스, j는 x보다 큰 마지막 인덱스를 찾음.
        if A[j] <= x:  # 그래서 모두 찾고, j에 다음 값이 들어와서 조건을 만족하면,
            i += 1  # i에 1을 더해주고,
            A[i], A[j] = A[j], A[i]  # 값을 바꿔준다.
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1  # i + 1을 return 하면...?!


def quickSort(A, l, r):
    if l < r:
        s = partition(A, l, r)  # i + 1 값이 들어간다.
        quickSort(A, l, s - 1)
        quickSort(A, s + 1, r)


test = [3, 2, 4, 6, 9, 1, 8, 7, 5]
quickSort(test, 0, len(test) - 1)
print(test)
