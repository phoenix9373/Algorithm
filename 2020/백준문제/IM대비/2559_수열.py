# 위치를 그대로 인덱스로 표현하는 것.
# 표현을 최대한 간결하게 하는 것이 핵심이다.
# 자료구조...!

N, K = map(int, input().split())
# N: 온도를 측정한 전체 날짜의 수 2 ~ 100,000
# K: 연속적인 날짜의 수.
arr = list(map(int, input().split()))  # 1과 N 사이 정수.

S = sum(arr[:K])
maxS = S
for i in range(N - K):
    tmpS = S - arr[i] + arr[K + i]
    if tmpS > maxS:
        maxS = tmpS
    S = tmpS
print(maxS)