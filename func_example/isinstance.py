# isinstance 활용법

a = [int(i) if i in '0123456789' else i for i in 'ab123sd2cdfas56']
print(a)

# 문자열과 숫자를 해보자.

str_list = [i for i in a if isinstance(i, int)]
int_list = [i for i in a if isinstance(i, str)]

print(str_list)
print(int_list)