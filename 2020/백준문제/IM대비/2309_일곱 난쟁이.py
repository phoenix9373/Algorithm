# 중복 값이 없는 조합.
# 조합이므로 순서 상관없이 중복되면 안된다...!
# 9C7 == 9C2: 총 36개.

arr = [int(input()) for _ in range(9)]
sel = [0] * 7

N = len(arr)
R = len(sel)
rep = []

def comb(idx, sidx):
    # back tracking
    if sum(sel) > 100:
        return

    if sidx == R:
        if sum(sel) == 100:
            global rep
            rep.append(sorted(sel))
        return

    for i in range(idx, N):
        sel[sidx] = arr[i]
        comb(i + 1, sidx + 1)

comb(0, 0)
for i in rep[0]:
    print(i)

'''
2
23
25
10
15
20
5
17
58
'''