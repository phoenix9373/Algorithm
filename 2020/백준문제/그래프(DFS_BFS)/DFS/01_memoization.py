# memo를 위한 리스트 생성
# memo[0]을 0으로, memo[1]은 1로 초기화함.
# 피보나지 fibo(0) = 0 , fibo(1) = 1인 조건을 맞춤.

# memoization의 핵심은 재귀 호출을 통한 중복된 함수 호출에서 벗어나
# 함수를 호출하면서 해당 값의 함수값을 cache에 저장하는 방식으로
# 전환하여 원하는 값(n)에 대한 함숫값을 cache에서 가져오는 것.
def fibo(n):
    global memo
    if n >= 2 and len(memo) <= n: # len(memo)는 중복 호출을 막기 위함.
        memo.append(fibo(n-1) + fibo(n-2))
    return fibo(n)

memo = [0, 1]

print(fibo(5))