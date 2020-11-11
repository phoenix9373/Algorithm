for tc in range(1, int(input())+1):
    line = input().split()
    stack = []
    result = 0
    for i in line:
        if '0' <= i <= '9':
            stack.append(int(i))
        elif i in '+*-/':
            if len(stack) < 2:
                result = 'error'
                break
            else:
                b = stack.pop()
                a = stack.pop()
                if isinstance(a, int) and isinstance(b, int):
                    if i == '+':
                        stack.append(a + b)
                    elif i == '*':
                        stack.append(a * b)
                    elif i == '-':
                        stack.append(a - b)
                    elif i == '/':
                        stack.append(a // b)
                else:
                    result = 'error'
                    break
        else:
            if len(stack) != 1:
                result = 'error'
                break
            else:
                result = stack.pop()
                break
    print('#{} {}'.format(tc, result))
