# 문자를 숫자로

def atoi(text):
    value = 0
    for i in range(len(text)):
        c = text[i]

        if '0' <= c <= '9': # 문자열의 ASCII 코드 값으로 비교한다. 따라서 문자열도 비교할 수 있다.
            digit = ord(c) - ord('0')
        else:
            break
        value = value*10 + digit
    return value

a = '17849'
a = atoi(a)
print(a)
print(type(a))