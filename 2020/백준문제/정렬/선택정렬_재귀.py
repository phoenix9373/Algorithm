def selectionSort(A):
    if len(A) == 1:
        return [A[0]]

    min_idx = 0
    for i in range(1, len(A)):
        if A[min_idx] > A[i]:
            min_idx = i
    A[0], A[min_idx] = A[min_idx], A[0]
    return [A[0]] + selectionSort(A[1:])


print(selectionSort([2, 3, 1, -1, 5, 193, 91, 84, 810, 50]))