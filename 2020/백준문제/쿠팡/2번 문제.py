# 키오스크: 1 ~ n
# 도착한 시간순으로 키오스크 매칭
# 가장 대기 많이 한 키오스크랑. 대기열을 큐로 구현하면 될 듯. 대기 시간이 동일하면 고유번호가 낮은 순서로.
# 모두 업무 중이면, 현재 가장 빨리 끝나는 키오스크로.
from datetime import datetime, timedelta


def solution(n, customers):
    times = [[datetime.strptime(info[:-3], "%m/%d %H:%M:%S"), timedelta(minutes=int(info[-2:]))] for info in customers]
    kiosks = [[name_num+1, 0, 0, 0, 0] for name_num, _ in enumerate(range(n))] # [키오스크 번호, 고객 도착 시간, 소요 시간, 대기 시간, 고객 수]
    print(kiosks)

    answer = 0
    return answer

solution(3, ["10/01 23:20:25 30", "10/01 23:25:50 26", "10/01 23:31:00 05", "10/01 23:33:17 24", "10/01 23:50:25 13", "10/01 23:55:45 20", "10/01 23:59:39 03", "10/02 00:10:00 10"])




#
#
# a =
# b = datetime.strptime("10/01 23:25:50", "%m/%d %H:%M:%S")
#
# c = b - a
# d = timedelta(minutes=5)
#
# print(c)
# print(c + d)
# print(c + d > c)