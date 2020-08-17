for c in range(1, int(input()) + 1):
    n = int(input())
    nums = list(map(int, input().split()))
    M = 0
    for i in range(n):
        for j in range(i+1, n):
            s = nums[i]*nums[j]
            s_2 = nums[i]*nums[j]
            cnt = 5 # 10**5 이하.
            while cnt > 0:
                a = s_2//(10**cnt)
                s_2 = s_2 % (10**cnt)
                b = s_2//(10**(cnt-1))
                if a > b:
                    break
                cnt = cnt - 1
                if (cnt == 0) and (M < s):
                    M = s
    if M == 0:
        result = -1
    else:
        result = M
    print(f'#{c} {result}')