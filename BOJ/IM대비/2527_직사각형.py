# 기준점을 대상으로 이동거리 측정.

def result(arr):
    a = arr[:4]
    b = arr[4:]
    a_x, a_y = a[2] - a[0], a[3] - a[1]
    b_x, b_y = b[2] - b[0], b[3] - b[1]
    d_x, d_y = abs(b[0] - a[0]), abs(b[1] - a[1])

    if d_x == a_x and d_y == a_y:
        res = 'c'
    elif d_x == a_x or d_y == a_y:
        res = 'b'
    elif d_x < a_x and d_y < a_y:
        res = 'a'
    else:
        res = 'd'

    return res

cases = [list(map(int,input().split())) for _ in range(4)]
case = []
for case_arr in cases:
    case.append(result(case_arr))

print(*case, sep='\n')