# filter 활용법

a = [int(i) if i in '0123456789' else i for i in 'ab123sd2cdfas56']
print(a)

# 문자열과 숫자를 가려보자.

# filter(func, iterable obj)

# filter를 실행할 때,
# iterable 객체의 요소 하나하나가 함수에
# 들어간다는 것을 유의해야한다.
def get_number(input_char):
    if isinstance(input_char, int):
        return True
    return False

def get_str(input_char):
    if isinstance(input_char, str):
        return True
    return False

int_list = filter(get_number, a)
str_list = filter(get_number, a)

print(int_list)
print(str_list)