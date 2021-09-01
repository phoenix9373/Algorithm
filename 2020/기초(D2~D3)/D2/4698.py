def prime_nums(n): # 10^6까지.
    if n < 2:
        return 0
    if n in [2, 3, 5, 7]:
        return n
    if n % 2 == 0:
        return 0
    l = round(n**0.5) + 1
    for i in range(3, l+1, 2):
        if n % i == 0:
            return 0
    return n
nums = [i for i in map(prime_nums, [j for j in range(10**6)]) if i]
for c in range(1, int(input())+1):
    d, a, b = map(int, input().split())
    L = list(filter(lambda x: a<=x<=b, nums))
    cnt = 0
    for k in L:
        if str(d) in str(k):
            cnt += 1
    print(f'#{c} {cnt}')