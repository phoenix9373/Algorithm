for tc in range(1, int(input()) + 1):
    string = ' '.join(input()).split()
    stack = []

    for c in string:
        if c in stack:
            stack.remove(c)
        else:
            stack.append(c)

    ans = ''.join(sorted(stack)) if stack else 'Good'
    print('#{} {}'.format(tc, ans))