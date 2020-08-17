
a = [int(i) if i in '0123456789' else i for i in 'ab123sd2cdfas56']


# 리스트를 뒤집고 싶다면?
print(a)
print(a[::-1]) # -1씩 한 스텝씩 이동.

# 리스트 문자열로 합치기
# 주의: 리스트 내 요소가 반드시 str type이어야한다.
b = list(map(str, a))

print(b)
print(''.join(b))
