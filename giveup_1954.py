t = int(input())

for case in range(1, t+1):
    n = int(input())

    nums = [[0]*n for i in range(n)] # n = 4

    k, l = 0, 0
    K, L = n-1, n-1
    x = 1
    # 0 1 2 3
    while (k < K) and (l < L):
        
        for i in range(L+1):
            print(x)
            nums[k][i] = x
            x += 1
        k += 1 

        for j in range(k, K+1):
            print(x)
            nums[j][L] = x
            x += 1
        L -= 1 

        if k <= K:
            for i in range(L, l-1, -1):
                print(x)
                nums[K][i] = x
                x += 1
            K -= 1
        if l <= L:
            for j in range(K, k-1, -1):
                print(x)
                nums[j][l] = x
                x += 1
            l += 1 # K=2, k=1, l=1, L=2
    
    print(f'#{case}')
    for i in nums:
        print(*i)