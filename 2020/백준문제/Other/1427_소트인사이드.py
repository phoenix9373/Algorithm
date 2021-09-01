n = list(input())

for i in range(len(n)-1):
    max_idx = i
    for j in range(i+1, len(n)):
        if n[max_idx] < n[j]:
            max_idx = j
    n[max_idx], n[i] = n[i], n[max_idx]

print(*n, sep='')