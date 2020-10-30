# DP(동적 계획법), Dynamic Programming
# 최적화 문제를 해결하는 알고리즘
# 1. 입력 크기가 작은 부분 문제들을 모두 해결한 후,
# 2. 그 해들을 이용하여 보다 큰 크기의 부분 문제들을 해결
# 3. 최종적으로 원래 주어진 입력의 문제를 해결

# 피보나치에 DP 적용하기: 부분 문제의 답으로부터 본 문제의 답을 얻을 수 있는 "최적 부분 구조"로 이루어져 있어 DP 적용 가능.
# 방법
# 1. 문제를 부분 문제로 분할
# 2. 1이 끝나면, 가장 작은 부분 문제부터 해결
# 3. 결과를 테이블에 저장하고, 테이블에 저장된 부분 문제의 해를 이용하여 상위 문제의 해를 차례대로 구함.

# 반복문만 활용.
def fibo2(n):
    # 작은 부분 해결 + 테이블 생성
    f = [0, 1] # f[0]=0, f[1]=1, f[2]=1, f[3]=2 등등..

    for i in range(2, n+1):
        f.append(f[i-1]+f[i-2])

    return f[n]

print(fibo2(5))


# DP를 구하는 2가지 방식
# 1. recursive 방식: overhead 발생 가능성
# 2. iterative 방식: Memoization을 재귀적 구조에 사용하는 것보다 반복적 구조로 DP를 구현한 것이 성능이 더 효율적.