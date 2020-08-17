def counting_sort(A, B, k):
    # A: 정렬 안된 리스트.
    # B: 정렬된 리스트.
    C = [0] * k

    # 카운팅
    for i in range(0, len(B)):
        C[A[i]] += 1
    
    # 누적
    for i in range(1, len(C)):
        C[i] += C[i-1]

    # 정렬
    for i in range(len(B)-1, -1, -1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1

    return B


a = [2,6,2,5,2,7,3,5,6,1]
b = [0] * len(a)
print(counting_sort(a, b, len(a)))
    
