def main():
    string = input()
    bomb = input()

    char = bomb[-1]
    stack = []
    n = len(bomb)

    for c in string:
        stack.append(c)
        if c == char and ''.join(stack[-n:]) == bomb:
            del stack[-n:]

    ans = ''.join(stack)
    if ans:
        print(ans)
    else:
        print('FRULA')

if __name__ == '__main__':
    main()