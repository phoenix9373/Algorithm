import sys
sys.stdin = open('input.txt', 'r')

while True:
    text = input()
    if text == '.':
        break

    stack = []
    ans = 'yes'
    for c in text:
        if c not in '( [ ] )'.split():
            continue
        if c in ['(', '[']:
            stack.append(c)
        else:
            if len(stack) == 0:
                ans = 'no'
                break
            else:
                if c == ')' and stack[-1] == '(':
                    stack.pop()
                elif c == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    ans = 'no'
                    break
    if len(stack):
        ans = 'no'
    print(ans)