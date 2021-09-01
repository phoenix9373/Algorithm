N = int(input())
maxV = 0
res = []

def count(first, second):
    global maxV, res
    f = [first, second]

    i = 1
    while True:
        tmp = f[i - 1] - f[i]  # 3번째 수.
        if tmp < 0: # 음수면 정지. 음수일때까지 반복. 양의 정수.
            if maxV < len(f):
                maxV = len(f)
                res = f
            return
        f.append(tmp) # 아니면 추가.
        i += 1

for i in range(N//2, N + 1):
    count(N, i)
print(maxV)
print(*res)