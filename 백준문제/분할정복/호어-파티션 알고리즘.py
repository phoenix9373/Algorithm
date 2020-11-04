def partition(A, l, r):
    p = A[l] # pivot: 기준이 되는 값.
    i = l + 1
    j = r
    while i <= j:
        while i <= j and A[i] <= p: i += 1
        while i <= j and A[i] >= p: j -= 1
        if i <= j:
            A[i], A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[l]
    return j # 분할할 지점의 인덱스