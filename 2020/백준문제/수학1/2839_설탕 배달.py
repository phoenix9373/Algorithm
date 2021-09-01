n = int(input())

def find(x):
    if x == 3 or x == 5:
        return 1
    cnt = x // 5
    rest = x - cnt * 5
    while cnt >= 0:
        if rest % 3 == 0:
            return cnt + rest // 3
        else:
            cnt -= 1
            rest += 5
    return -1

print(find(n))