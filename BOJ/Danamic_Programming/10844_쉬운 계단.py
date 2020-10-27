# N = int(input())
#
# dp = [[0] * 10 for _ in range(101)]
#
# dp[1] = [1] * 10
#
# for n in range(2, N + 1):
#     for i in range(10):
#         if i == 0:
#             dp[n][i] == dp[n - 1][i + 1]
#         elif 0 < i < 9:
#             dp[n][i] = dp[n - 1][i - 1] + dp[n - 1][i + 1]
#         else:
#             dp[n][i] = dp[n - 1][i - 1]
