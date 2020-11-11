# 개수가 짝수이고, 모든 문자의 개수가 짝수일 때.
# 개수가 홀수이고, 한 문자를 제외한 나머지가 짝수일 때.
from collections import Counter

t = input()
n = len(t)


def sol(name):
    if len(name) == 1:
        return name

    counts = Counter(name)
    left = ''
    char = ''

    if n % 2 == 0:
        for k, v in counts.items():
            if v % 2:
                return False
            left += k * (v // 2)
    elif n % 2 == 1:
        tmp = 0
        for k, v in counts.items():
            if v % 2:
                char = k
                tmp += 1
            left += k * (v // 2)
        if tmp > 1:
            return False

    left = ''.join(sorted(left))
    right = left[::-1]
    return left + char + right


ans = sol(t)
if ans:
    print(ans)
else:
    print("I'm Sorry Hansoo")