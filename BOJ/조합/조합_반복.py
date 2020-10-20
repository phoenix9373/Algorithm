arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
N = 9
R = 7
# N개 중에 R개 뽑기 - 조합

sel = [0] * R # 뽑은 값

def combination(idx, sidx):
    if sidx == R:
        print(sel)
        return

    for i in range(idx, N): # 다음 함수를 넘겨줄 때, idx값이 아니라 i 값을 넘겨줬다.
        sel[sidx] = arr[i]  # 즉, i 이전의 값은 고려치 않음!
        combination(i + 1, sidx + 1)

combination(0, 0)