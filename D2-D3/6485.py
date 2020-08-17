import sys

sys.stdin = open("test.txt", "r")
for test_case in range(1, int(input()) + 1):
    n = int(input())
    case = [0 for _ in range(5000)]
    for _ in range(n):
        a, b = map(int, input().split())
        for i in range(a, b+1):
            case[i-1] += 1
    p = int(input())
    c = [int(input())-1 for _ in range(p)]
    result = [case[i] for i in c]
    print(f'#{test_case}', *result)
    



# 버스정류장, 1~5000까지 번호
# 버스노선, N개가 있다.
# i번째 버스 노선은 (번호가 Ai 이상, Bi 이상인 모든 정류장)만을 다니는 버스 노선.
# P개의 버스 정류장에 대해 각 정류장에 '몇 개의 버스 노선이 다니는지'


# k에서 각 값들을 -1씩 해서 인덱스로 사용한다.
# 앞에서 a, b에 대해 -1씩 해줬으므로 같이 인덱스로 활용한다.
# L에서 max(k)만큼 만들어주고, 각 index에 대해 +1씩 한다.