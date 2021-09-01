arr = [1, 2, 3, 4]
N = 4
R = 2
# N개 중에 R개 뽑기 - 조합

sel = [0] * R # 뽑은 값

def combination(idx, sidx):
    if sidx == R:
        print(sel)
        return

    if idx == N:
        return

    sel[sidx] = arr[idx]
    # 뽑고 가고
    combination(idx+1, sidx+1)
    # 안 뽑고 가고
    combination(idx+1, sidx)