N = int(input())
arr = list(map(int, input().split()))

max_val = 0
cnt = 0
tmp = arr[0]
# 증가
for i in arr:
    if i >= tmp:
        cnt += 1 # 카운트 늘리고,
        tmp = i  # 지금 값으로 바꿔주고.
    else:
        cnt = 1 # 작으면 초기화.
        tmp = i # 시작점을 지금 값으로.
    if cnt >= max_val:
        max_val = cnt
# 감소
cnt = 0
tmp = arr[0]
for i in arr:
    if i <= tmp:
        cnt += 1 # 카운트 늘리고,
        tmp = i  # 지금 값으로 바꿔주고.
    else:
        cnt = 1 # 크면 초기화.
        tmp = i # 시작점을 지금 값으로.
    if cnt >= max_val:
        max_val = cnt

print(max_val)