w, h = map(int, input().split())
p, q = map(int, input().split()) # p, q
t = int(input())

# p, q 자체에 값을 더하거나 뺀다.
def move(s, length):
    d = 1
    for i in range(t % (2*length)):
        if s + d > length or s + d < 0:
            d *= -1
        s += d
    return s

p = move(p, w)
q = move(q, h)

print(p, q)