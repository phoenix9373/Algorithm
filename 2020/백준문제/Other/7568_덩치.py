n = int(input())

persons = [list(map(int, input().split())) for i in range(n)]
count = [1] * n
for i in range(n):
    for j in range(n):
        if persons[i][0] < persons[j][0] and persons[i][1] < persons[j][1]:
            count[i] += 1
print(*count)