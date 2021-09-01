for _ in range(10):
    tc, n = map(int, input().split())
    arr = list(map(int, input().split()))  # 간선
    ch1 = [0] * 100 # 출발점을 인덱스로 도착점 번호를 저장.
    ch2 = [0] * 100

    # 데이터 저장
    for i in range(n):
        n1 = arr[i*2]   # 출발
        n2 = arr[i*2+1] # 도착
        if ch1[n1]==0:
            ch1[n1] = n2 # n1의 첫번째 경로.
        else:
            ch2[n1] = n2 # n1의 두번째 경로.

    # 찾아가는 방법..?
