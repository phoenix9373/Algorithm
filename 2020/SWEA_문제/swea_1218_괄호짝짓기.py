def check(bracket):
    stack = []
    for i in range(len(bracket)):
        t = bracket[i]
        if t in '{(<[':
            stack.append(t)
        elif t in '}]>)':
            if len(stack) == 0:
                return 0
            tmp = stack.pop()

            if tmp == '{' and t =='}':
                continue
            elif tmp == '(' and t ==')':
                continue
            elif tmp == '[' and t ==']':
                continue
            elif tmp == '<' and t =='>':
                continue
            return 0
    return 1

for tc in range(1, 11):
    n = int(input())
    s = input()
    result = check(s)
    print('#{} {}'.format(tc, result))