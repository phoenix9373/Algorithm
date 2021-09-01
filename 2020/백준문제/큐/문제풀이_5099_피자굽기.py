for tc in range(1, int(input() + 1)):
    N, M = map(int, input().split()) # N: 화덕의 크기, M: 피자수
    pizza = [0] + list(map(int, input().split())) # 인덱스를 맞춰줌

    # q 생성
    oven = [i for i in range(1, N + 1)] # 피자 번호
    pos = N + 1 # 추가될 피자 번호.

    while len(oven) > 1:
        num = oven.pop(0) # 맨 처음 것 가져오기.
        pizza[num] = pizza[num] // 2
        if pizza[num]: # 아직 치즈가 남아있으면
            oven.append(num) #
        else:
            if pos <= M:
                oven.append(pos)
                pos += 1
        print(oven[0])