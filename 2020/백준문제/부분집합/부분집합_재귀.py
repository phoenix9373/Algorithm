# 부분집합

arr = [i for i in range(10)]
sel = [0] * len(arr)
standard = 10

# 부분집합 중 합이 10 이하인 것들만.
def powerset(idx, cumsum):

    if cumsum > standard:
        return

    if idx == len(arr):
        for i in range(len(arr)):
            if sel[i]:
                print(arr[i], end=' ')
        print()
        return

    sel[idx] = arr[idx]
    powerset(idx + 1, cumsum + arr[idx])
    sel[idx] = 0
    powerset(idx + 1, cumsum)


powerset(0, 0)