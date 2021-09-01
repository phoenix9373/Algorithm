def itoa(digit):
    arr = []
    while digit > 0:
        value = digit % 10
        digit = digit // 10
        arr.append(chr(value + ord('0')))

    return ''.join(arr[::-1])

print(itoa(1325))
print(type(itoa(1325)))
