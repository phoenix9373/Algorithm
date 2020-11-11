for tc in range(1, int(input()) + 1):
    string = input()

    mod = {'b': 'd', 'd': 'b', 'p': 'q', 'q': 'p'}

    ans = ''
    for c in string[::-1]:
        ans += mod[c]
    print('#{} {}'.format(tc, ans))