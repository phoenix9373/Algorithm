for tc in range(int(input())):
    info = input()
    stack = []

    for c in info:
        if c == '(':
            stack.append(c)
        else:
            if len(stack) == 0:
                print('NO')
                break
            stack.pop()
    else:
        if stack:
            print('NO')
        else:
            print('YES')