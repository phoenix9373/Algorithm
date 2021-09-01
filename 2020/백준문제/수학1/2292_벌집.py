x = int(input())

n = 0.5 + pow(12*x-3, 0.5) / 6
test = round(n) - 2
while test < n:
    test += 1
    if test >= n:
        print(test)
        break