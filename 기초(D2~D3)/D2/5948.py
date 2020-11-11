for c in range(1, int(input())+1):
    seven = list(map(int, input().split()))
    sums = sorted(set([x+y+z for x in seven for y in seven for z in seven if x!=y and y!=z and z!=x]))
    print(f'#{c} {sums[-5]}')
