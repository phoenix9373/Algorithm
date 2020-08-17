for c in range(1, int(input())+1):
    t = input()
    r = ''.join(list(filter(lambda x: x not in ['a','e','i','o','u'], t)))
    print(f'#{c} {r}')