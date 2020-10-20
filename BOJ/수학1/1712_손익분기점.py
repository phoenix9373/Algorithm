a, b, c = map(int, input().split())
result = -1
if b < c:
    result = a // (c-b) + 1
    print(result)
else:
    print(result)