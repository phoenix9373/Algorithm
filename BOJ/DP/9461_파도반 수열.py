n = int(input())

def pado(x):
    f = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12]
    if x > 11:
        for i in range(12, x+1):
            f.append(f[i-1] + f[i-5])
    return f[x]

for i in range(n):
    num = int(input())
    print(pado(num))