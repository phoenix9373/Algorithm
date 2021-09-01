# 1. X % 3 == 0 이면, 3으로 나눈다.
# 2. X % 2 == 0 이면, 2로 나눈다.
# 3. 1을 뺀다.

# 정수 N이 주어졌을 때, 위 연산 3가지를 이용해서 1을 만든다.
# 연산을 사용하는 횟수의 최솟값을 출력.


N = int(input())

dp = [0, 0, 1, 1, 2, 3, 2, 3, 3, 2, 3, 4, 3]


def func(n):
    print(n)
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n == 3:
        return 1

    a, b, c = [pow(2, 32) for _ in range(3)]
    if n % 3 == 0:
        a = func(n / 3) + 1
    if n % 2 == 0:
        b = func(n / 2) + 1
    c = func(n + 1) + 1

    return min(a, b, c)


print(func(4))