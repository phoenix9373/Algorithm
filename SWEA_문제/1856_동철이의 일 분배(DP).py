import sys
sys.stdin = open('input2.txt', 'r')

for t in range(int(input())):
    n = int(input())
    m = 1<<n # 부분집합 개수
    d = [0]*m # 방문?
    p = [[*map(lambda x:x/100,map(int,input().split()))] for _ in range(n)]
    d[0] = 1
    for mask in range(m):
        x = sum(1 for i in range(n) if mask&(1<<i)) # 비트 중 1의 개수의 합. 8은 1000이므로 x = 1이다.
        for j in range(n): # 각 부분집합마다 한 열 반복.
            if mask&(1<<j) == 0:
                d[mask|(1<<j)] = max(d[mask|(1<<j)],d[mask]*p[x][j])
    print(*p, sep='\n')
    print(d)
    print(f'#{t+1} {d[-1]*100:.6f}')