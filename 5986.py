def is_prime(n):
    if n < 2:
        return False
    if n in [2, 3, 5, 7]:
        return n
    if n % 2 == 0:
        return False
    l = round(n**0.5) + 1
    for i in range(3, l, 2):
        if n % i == 0:
            return False
    return n
nums = list(filter(lambda x: x!=False, map(is_prime, [i for i in range(1000)])))

for test_case in range(1, int(input()) + 1):
    k = int(input())
    cnt = 0
    new_nums = list(filter(lambda x: x<k, nums))
    for x in new_nums:
        for y in new_nums:
            if x <= y:
                for z in new_nums:
                    if y <= z:
                        if x+y+z==k:
                            cnt += 1
    print(f'#{test_case} {cnt}')