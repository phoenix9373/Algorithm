# 또 다른 방법

memo = {0:0, 1:1}

# memoization + 재귀 함수 사용.
def fibo(n):
    global memo

    if n not in memo:
        memo[n] = fibo(n-1) + fibo(n-2)

    return memo[n]

print(fibo(7))

# pythonic한 피보나치 수열 구하기

def fibo_exp(n):
    a, b = 1, 0
    for i in range(n):
        a, b = b, a + b
    return b

print(fibo_exp(7))