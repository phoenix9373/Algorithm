# bit_mask로 하는 방법도 있다.

arr = [1, 2, 3]
N = 3

sel = [0] * N # 사용.


def perm(idx, check):
    if idx == N:
        print(sel)
        return

    for i in range(N): # 원소의 개수만큼 반복할 것.
        if (check & (1<<i)) != 0: # 이전에 사용한 원소 사용 X. -> 이걸 어떻게 체크?
            continue

        sel[idx] = arr[i]
        perm(idx + 1, check | (1 << i)) # '또는'이라는 비트 연산자가 들어갔으므로, check에 저장된 1인 bit가 다음 함수 호출에서는 제외된다.

            # ...

perm(0, 0)