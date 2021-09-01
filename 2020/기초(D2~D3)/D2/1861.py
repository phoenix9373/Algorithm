# 상하좌우 이동 가능, 현재 방 숫자가 이동하려는 방의 숫자보다 1 작다.
# N^2의 방에 각각 1~N^2의 숫자가 중복없이 적힘.
# 이동거리가 가장 긴 방의 숫자.
# 상하좌우로 검색해서 가능한 방향을 모두 탐색.
# 탐색하는 동안 cnt를 세서 max값을 저장.
# total_cnt를 세서 각 방의 cnt 중 max 값을 저장.
# '#c 방번호 최대방개수'
# 갈수있는 방의 개수가 최대인 방이 여러개면 가장 작은 수를 출력.
import sys
sys.stdin = open('input.txt', 'r')
def recursive(arr, x, y, cnt=1): # x = j, y = i
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    l = len(arr) - 1
    for k in range(4):
        X = x + dx[k]
        Y = y + dy[k]
        if (0<=X<=l) and (0<=Y<=l) and (arr[Y][X] - arr[y][x] == 1):
            cnt += 1
            return recursive(arr, X, Y, cnt)
    return cnt
for c in range(1, int(input())+1):
    n = int(input())
    N = [list(map(int, input().split())) for _ in range(n)]
    total = [[N[i][j], recursive(N, j, i)] for i in range(n) for j in range(n)]
    a, b = sorted(total, key=lambda x: (-x[1], x[0]))[0]
    print(f'#{c} {a} {b}')

        # 재귀함수를 활용해서 풀 수 있지 않을까?
