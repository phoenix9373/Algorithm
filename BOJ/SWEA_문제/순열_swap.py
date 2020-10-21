arr = [1,2,3]
N = 3


def perm(idx):

    if idx == N:
        print(arr)
        return
    # arr를 가지고 자리를 바꾸면서 수행.
    for i in range(idx, N):
        arr[idx], arr[i] = arr[i], arr[idx]
        perm(idx + 1)
        arr[idx], arr[i] = arr[i], arr[idx] # 원상복귀

perm(0)