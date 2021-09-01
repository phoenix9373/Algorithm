# bit mask 활용하기

n, m = map(int, input().split()) # 4 2
arr = [i for i in range(1, n + 1)] # 1, 2, 3, 4
sel = [0] * m # [0, 0]
sorted_case = []

def perm(idx, check):
    global sorted_case

    if idx == m: # idx가 m일 때까지만 반복.
        if sorted(sel) not in sorted_case:
            sorted_case.append(sorted(sel))
        return

    for i in range(n): # 원소의 개수만큼 반복.
        # 예외사항, 중복 피하기.
        if check & (1<<i) != 0: # check 값이 0001이면 1인 원소 제외.
            continue

        sel[idx] = arr[i] #
        # check에는 bit 연산이 들어갈 것.
        perm(idx + 1, check | (1<<i)) # check에 1<<i 를 더해줌. 즉, 다음 함수 호출에서 현재 함수에서 사용한 원소 제외.
perm(0, 0)
for case in sorted_case:
    print(*case)