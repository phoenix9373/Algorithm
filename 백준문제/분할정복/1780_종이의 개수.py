# arr 자르기, n = len(arr), k = int(n / 3)
# 0 - 2, 3 - 5, 6 - 8
# arr0 = [[arr[i][j] for i in range(3)] for j in range(3)]
# arr1 = [[arr[i][j] for j in range(3*1, 3*2)] for i in range(3)]
# arr1 = [[arr[i][j] for j in range(i*k, (i+1)*k] for i in range(j*k, (j+1)*k]
# len(arr) = 27이라고 하면, 0부터 9까지.
# 모든 원소가 같으면 끝. 아니면..?!
N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
ans = {'0': 0, '1': 0, '-1': 0}


