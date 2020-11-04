import sys
N = int(sys.stdin.readline())

def VPS(s):
    stack = []

    for idx, i in enumerate(s):
        if i == '(':
            stack.append(i)
        else:
            if len(stack) == 0:
                return 'NO'
            else:
                stack.pop()

    if len(stack) == 0:
        return 'YES'
    else:
        return 'NO'

for _ in range(N):
    tmp = sys.stdin.readline()
    print(VPS(tmp))