def multi(n):
    l = round(n**0.35) + 1
    for k in range(1, l):
        if k**3 == n:
            return k
    return -1
for c in range(1, int(input())+1):
    x = multi(int(input()))
    print(f'#{c}' ,x)
