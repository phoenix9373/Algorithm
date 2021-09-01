for tc in range(1, 11):
    n = int(input())
    text = input()

    stack = []
    output = []
    prime = {'(' : 0, '+' : 1, '*' : 2}

    for i in text:
        if i == '(':
            stack.append(i)
            continue
        elif i == ')':
            while True:
                tmp = stack.pop()
                if tmp == '(':
                    break
                else:
                    output.append(tmp)
            continue

        if '0' <= i <= '9':
            output.append(i)
            continue
        else: # +, *
            if len(stack) == 0:
                stack.append(i)
            else: # 스택이 안 비어있고, +나 *이 들어옴.
                while True:
                    if len(stack) == 0:
                        stack.append(i)
                        break
                    tmp = stack[-1]
                    if prime[i] <= prime[tmp]:
                        output.append(stack.pop())
                    else:
                        stack.append(i)
                        break
    while stack:
        output.append(stack.pop())

    cal_stack = []
    for i in output:
        if '0' <= i <= '9':
            cal_stack.append(int(i))
        else:
            a = cal_stack.pop()
            b = cal_stack.pop()
            if i == '+':
                cal_stack.append(a+b)
            elif i == '*':
                cal_stack.append(a*b)
    print('#{} {}'.format(tc, *cal_stack))