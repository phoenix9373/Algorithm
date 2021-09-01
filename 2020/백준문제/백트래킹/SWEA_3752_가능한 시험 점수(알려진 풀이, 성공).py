for tc in range(1, int(input()) + 1):
    N = int(input())
    score = list(map(int, input().split()))

    # 점수를 index로 활용하기 위해 배열을 생성
    arr = [0] * (sum(score) + 1)

    # 뒤쪽부터 하나씩 탐색하면서 가능한 점수의 index에 1을 할당
    # 0은 항상 가능하므로 1로 초기화
    arr[0] = 1
    for s in score:
        for i in range(len(arr)-1, -1, -1):
            if arr[i] == 1:
                arr[i + s] = 1
    print(arr.count(1))