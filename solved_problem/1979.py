# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제 
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''

import sys


'''
      아래의 구문은 input.txt 를 read only 형식으로 연 후,
      앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
      여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
      아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.

      따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
      아래 구문을 사용하기 위해서는 import sys가 필요합니다.

      단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    # 문제 해석
    # 0은 검은색, 1은 하얀색. 길이가 k인 단어는 1이 연속으로 정확히 k개만 있어야한다.
    # 배열 크기인 N은 5 ~ 15, 단어 크기인 K는 2 ~ N이다.
    n, k = map(int, input().split())
    
    # 가로줄을 검사하면서, 세로줄에 대한 자료를 넘겨준다.
    # 중첩으로 가로줄에 대한 리스트, 세로줄에 대한 리스트를 넘겨준다.
    horizon = []
    vertical = []

    for i in range(n):
        nums = list(map(int, input().split()))
        horizon.append(nums)
        if len(vertical) == 0:
            vertical = [[i] for i in nums]
        else:
            for idx, j in enumerate(nums):
                vertical[idx].append(j)

    # 각 세로줄, 가로줄 생성완료.
    # 앞부터 확인하여 카운트를 센다.
    # k보다 큰 연속 값에 대해 어떻게 처리할까?
    # sum을 보고 먼저 안되면 패스하는 로직 추가 - 반복문 줄이기.
    # 

    def count(count_list):
        cnt = 0
        total = 0
            
        for i in count_list:
            k_list = []
            j_sum = 0
            for j in i: # i는 세로 또는 가로 한줄.
                if j:
                    j_sum += 1
                else:
                    if j_sum:
                        k_list.append(j_sum)
                    j_sum = 0
            else:
                k_list.append(j_sum)
            
            total += k_list.count(k)

            # 로직을 먼저 생각해보자.
            # 연속으로 k개 숫자가 오면 +1, 한 줄에 2번 이상 가능함.
            # 만약 카운트가 k가 되면, total에 +1을 한다.
            # 연속인 숫자의 합을 구하는 로직?
            # 0이 나올때까지 또는 끝날 때까지 연속인 숫자의 합을 구하는 로직을 구한다.
            # 연속인 숫자의 합을 어떤 리스트에 넣고
            # 그 숫자의 합이 k인 것의 개수를 센다. list.count(k)


        
        return total
    
    h_cnt = count(horizon)
    v_cnt = count(vertical)
    total = h_cnt + v_cnt

    print(f'#{test_case} {total}')
    
    # ///////////////////////////////////////////////////////////////////////////////////
