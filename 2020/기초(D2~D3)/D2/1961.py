for c in range(1, int(input())+1):
    n = int(input())
    x_arr = [list(map(int, input().split())) for _ in range(n)]
    
    def make(arr):
        l = len(arr)
        new = [[0]*l for _ in range(l)]
        c_s, c_l = 0, l-1
        r_s, r_l = 0, l-1
        if l % 2:
            new[l//2][l//2] = arr[l//2][l//2]
        while c_s<c_l and r_s<r_l:
            l = c_l - c_s + 1
            for k in range(l):
                new[r_s+k][c_l] = arr[r_s][c_s+k]
            for k in range(l):
                new[r_l][c_l-k] = arr[r_s+k][c_l]
            for k in range(l):
                new[r_l-k][c_s] = arr[r_l][c_l-k]
            for k in range(l):
                new[r_s][c_s+k] = arr[r_l-k][c_s]
            c_s += 1
            c_l -= 1
            r_s += 1
            r_l -= 1
        return new
    arr_90 = make(x_arr)
    arr_180 = make(arr_90)
    arr_270 = make(arr_180)
    print(f'#{c}')
    for i in range(n):
        for arr_t in [arr_90, arr_180, arr_270]:
            print(*arr_t[i], end=' ', sep='')
            if arr_t == arr_270:
                print()