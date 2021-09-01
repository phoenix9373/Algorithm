arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 재귀로..!
# visited와 sel을 사용하는 이유.
# visited는 한 번의 cycle에서 이전에 선택한 값을 선택하지 않도록 하기 위함.
# sel은 한 번의 cycle 안에서 row의 개수 또는 원소 개수만큼 돌면서
# 순서에 따른 원소를 선택할 때, 각각의 호출에서 어떤 값을 어떤 순서로 선택할지 저장하는 용도
n = len(arr)
visited = [[0] * n for _ in range(n)]
sel = [0] * n

def perm(row, idx): # row는 arr에서 각 행마다 한 개씩 선택할 건데 다음 값을 넘겨줄 때 +1한다.
    # idx는 한 번의 함수 호출 동안 선택할 값.
    # idx는 0, 1, 2, 3 으로 증가하므로 각각의 함수 호출에서 해당 순서 index에 값을 준다. sel[idx] = ?

    if row == n:
        print(sel) # N이 되는 순간 이미 sel에 값이 채워져있음.
        print()
        return # return 조건을 주지 않으면 마지막 함수 호출 시 아래 코드까지 실행함.

    for i in range(n): # 한 번의 호출에서 각 col 개수인 3번 반복.
        if visited[row][i] == 0: # 해당 row에서 하나를 선택하면,
            sel[idx] = arr[row][i] # 그 값으로 sel을 채우고,
            for j in range(n): # 해당 col을 모두 1로 채운다.
                visited[j][i] = 1
            perm(row + 1, idx + 1) # 그 다음, 다음 행에서 sel의 다음 index 값을 채운다.
            for j in range(n): # 중요!!!!!!
                visited[j][i] = 0 # 함수가 호출되면서 안으로 들어갈 때, visited는 채워진 상태였다.
                # 첫번째 행의 다른 col에 있는 원소의 조합도 보려면
                # 이전 값을 초기화해야한다. 즉, 함수 호출 과정을 이용한 초기화 조건 삽입.

perm(0, 0)