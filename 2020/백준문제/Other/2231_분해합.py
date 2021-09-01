T = int(input())

def n_sum(k, s=0):
    if k == 0:
        return int(s)
    s += k % 10
    k = (k - k % 10)/10
    return n_sum(k, s)

L = [i for i in range(T) if (i+n_sum(i))==T]
if L:
    print(min(L))
else:
    print(0)
print(len(str(T)))