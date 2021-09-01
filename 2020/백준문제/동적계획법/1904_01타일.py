# a<<b: << 연산자는 a를 b번 왼쪽으로 shift시킨다.
# arr = []
# for i in range(1<<n): # 자리수가 n인 값의 부분집합 수.
#     k = ''
#     for j in range(n):
#         if i & (1<<j):
#             k = '1' + k
#         else:
#             k = '0' + k
#     arr.append(k)
import sys
n = int(sys.stdin.readline())
def dp(x):
    f = [0] * 1000001
    f[1], f[2] = 1, 2
    for i in range(3, x+1):
        f[i] = (f[i-1] + f[i-2]) % 15746
    return f[x]
print(dp(n))