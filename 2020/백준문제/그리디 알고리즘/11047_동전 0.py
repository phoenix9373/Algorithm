N, K = map(int, input().split())

cnt = 0
coins = [int(input()) for _ in range(N)]

for i in range(len(coins) - 1, -1, -1):
    coin = coins[i]
    j = 1
    while K >= coin * j:
        j += 1
    cnt += j - 1
    K -= coin * (j - 1)
    if K == 0:
        break

print(cnt)

# n, k = list(map(int, input().split()))
#
# arr = []
# for i in range(n):
#     a = int(input())
#     arr.append(a)
#
# count = 0
# for i in range(n):
#     count += k // arr[-1 - i]
#     k = k % arr[-1 - i]
#
# print(count)