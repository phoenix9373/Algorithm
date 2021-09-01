# 조합으로 해야 시간 초과 X
# 시간이 오래 걸린 이유, 조합으로 r개를 뽑는데 r개 모두를 다 구하면서 함.
# 병훈이 코드와의 차이
# - 병훈이 코드는 n개 중 n개로 이루어진 조합을 찾아가는 중에 값을 비교하면서 가지치기함.
# - 내꺼는 n개 중 r개를 뽑는 조합에서 r은 1 ~ n까지 모든 크기의 조합을 다 구해가면서 함.(가지치기 없음.)

def combination(idx, sidx):
    if sidx == R:
        global ans
        if sum(sel) >= B and sum(sel) - B < ans:
            ans = sum(sel) - B
        return

    for i in range(idx, N):
        sel[sidx] = arr[i]
        combination(i + 1, sidx + 1)

for tc in range(1, int(input()) + 1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = pow(2, 30)
    for i in range(1, N + 1):
        R = i
        sel = [0] * R
        combination(0, 0)

    print('#{} {}'.format(tc, ans))