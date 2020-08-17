def check(text):
    if len(text) < 2:
        return 'Exist'
    if text[0] == '*' or text[-1] == '*':
        return 'Exist'
    if text[0] == text[-1]:
        if text[1] == '*' or text[-2] == '*':
            return 'Exist'
        return check(text[1:-1])
    else:
        return 'Not exist'
for c in range(1, int(input())+1):
    result = check(input())
    print(f'#{c} {result}')