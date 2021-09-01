A, B, c = map(int, input().split())

# 1. 표준 라이브러리 활용
ans = pow(A, B, c)
print(ans)


# 2. 아까는 왜 안됐지??
def power(a, b):
    if b == 1:
        return a % c
    else:
        tmp = power(a, b // 2)
        if b % 2:
            return tmp * tmp % c
        else:
            return tmp * tmp * a % c


print(power(A, B))