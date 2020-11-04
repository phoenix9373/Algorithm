# str1 = input()
# str2 = input()
#
# dp = [[0, 0] for _ in range(len(str1))]
#
# for i in range(len(str1)):
#     for j in range(len(str2)):
#         if str1[i] == str2[j]:
#             if i == 0:
#                 dp[i][0] = 1
#                 dp[i][1] = j
#                 continue
#
#             tmp = 0
#
#             for k in range(i - 1, -1, -1):
#                 if j > dp[k][1] and tmp < dp[k][0]:
#                     tmp = dp[k][0]
#             dp[i][0] = tmp + 1
#             dp[i][1] = j