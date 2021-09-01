for _ in range(4):
    info = list(map(int, input().split()))
    arr = sorted([info[:4], info[4:]], key=lambda x: x[0])
    x1, y1, p1, q1 = arr[0]
    x2, y2, p2, q2 = arr[1]  # 항상 x1 < x2

    ans = ''


    def sol():
        global ans
        if p1 < x2 or q1 < y2 or q2 < y1:
            ans = 'd'
            return
        if (p1, q1) == (x2, y2) or (p1, y1) == (x2, q2) or (x1, y1) == (p2, q2) or (x1, q1) == (p2, y2):
            ans = 'c'
            return
        if x2 == p1 and (y1 <= y2 < q1 or y1 < q2 <= q1):
            ans = 'b'
            return
        if q1 == y2 and (x1 <= x2 < p1):
            ans = 'b'
            return
        if y1 == q2 and (x1 <= x2 < p1):
            ans = 'b'
            return
        ans = 'a'
        return


    sol()
    print(ans)
