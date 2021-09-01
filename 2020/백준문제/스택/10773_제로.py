k = int(input())
stack = [0]
for _ in range(k):
    n = int(input())
    if n != 0:
        stack.append(n)
    else:
        stack.pop()

print(sum(stack))