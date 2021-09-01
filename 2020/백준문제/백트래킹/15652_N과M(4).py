n, m = map(int, input().split())
arr = [i for i in range(1, n + 1)]
sel = [0] * m

def perm(idx, k):

    if idx == m:
        print(*sel)
        return

    for i in range(k, n): # k 값을 줘서 현재 함수에서 선택한 원소를 기준으로 그 원소 및 이후의 원소를 선택할 수 있게.
        sel[idx] = arr[i]
        perm(idx + 1, i)
perm(0, 0)