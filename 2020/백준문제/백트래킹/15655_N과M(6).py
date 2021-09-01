def perm(idx, check, k):

    if idx == m:
        print(*sel)
        return

    for i in range(k, n): # 원소를 1개를 선택할 때마다 이후에는 선택한 원소의 우측부터 탐색
        if check & (1<<i) !=0:
            continue

        sel[idx] = arr[i]
        perm(idx + 1, check | (1<<i), i)

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split()))) # 받는 숫자들.
sel = [0] * m # 출력
perm(0, 0, 0)