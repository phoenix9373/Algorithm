# # arr = [3,6,7,1,5,4]

# # n = len(arr)

# # for i in range(1<<n): # 부분집합의 총 개수. 2^n개
# #     # total = 0
# #     for j in range(n): # 원소의 개수만큼 해당 원소가 1인지 0인지 조사.
# #         if i & (1<<j): # &는 비트 연산자.
# #             print(arr[j], end= " ")
# #     # if total == 0:
# #         # return 'YES'
# #     print()


def check(a):
        s=0
        e=len(a)-1
        if len(a) < 2:
            return a
        if a[s] == a[e]:
            return a[s] + check(a[s+1:e]) + a[e]
print(check('abcba'))