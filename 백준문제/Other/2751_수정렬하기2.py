# 카운팅 정렬로 풀기(선형시간의 시간복잡도)
# nums는 1,000,000 이하의 수
import sys
n = int(sys.stdin.readline())
count = [0] * 10001 # 1만 이하 정수.

# count 세기 + 누적.
for i in range(n):
    count[int(sys.stdin.readline())] += 1

for j in range(len(count)):
    while count[j] > 0:
        print(j)
        count[j] -= 1