def perm(idx, check):

    if idx == m:
        print(*sel)
        return

    for i in range(n): # n개 원소. 3개이면 1 << i는 100, 010, 001이 된다.
        if check & (1<<i) != 0: # 해당 원소가 있으면 건너뜀
            continue

        sel[idx] = arr[i]
        perm(idx + 1, check | (1<<i)) # check에 이번에 추가한 원소를 추가함.


n, m = map(int, input().split())
arr = sorted(list(map(int, input().split()))) # 받는 숫자들.
sel = [0] * m # 출력
perm(0, 0)