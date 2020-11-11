x = input().split('-')
ans = 0

for i in x[0].split('+'):
    ans += int(i)

for i in x[1:]:
    for j in i.split('+'):
        ans -= int(j)

print(ans)