import sys
sys.stdin = open('input.txt', 'r')
for tc in range(1, int(input())+1):
    n = int(input())
    nums = list(map(int, input().split()))
    m = sum(nums)/n
    k = list(filter(lambda x: x <= m, nums))
    print(f'#{tc} {len(k)}')