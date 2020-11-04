import sys
n = int(sys.stdin.readline())
orders = [sys.stdin.readline().strip() for _ in range(n)]
stack = []

def push(x):
    stack.append(x)


def pop():
    if len(stack) < 1:
        return -1
    else:
        return stack.pop()


def size():
    return len(stack)


def empty():
    if len(stack) < 1:
        return 1
    else:
        return 0


def top():
    if len(stack) < 1:
        return -1
    else:
        return stack[-1]


for o in orders:
    if 'push' in o:
        o, num = o.split()
        num = int(num)
        push(num)
    elif o == 'pop':
        print(pop())
    elif o == 'size':
        print(size())
    elif o == 'empty':
        print(empty())
    elif o == 'top':
        print(top())