for c in range(1, int(input())+1):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    result = [i for i in range(1, n+1) if i not in nums]
    print(f'#{c}', *result)