# 피보나치 수열 + Memoization
# fibo(n)의 값을 계산하자마자 저장하면 O(n)으로 시간복잡도를 줄일 수 있다.
# 0 1 1 2 3 5 8 13

def fibo2(n):
    if n >= 2 and len(memo) <= n:
        memo.append(fibo2(n-1) + fibo2(n-2))
    return memo[n]

memo = [0, 1] # 참조형(RW). 즉, 모든 함수에서 참조하여 읽고 쓸 수 있다. 바꿀 수 있다. mutable
ans = 0       # 일반변수, 값형(R). immutable
print(fibo2(10))