arr = [i for i in range(1, 11)]
N = len(arr)
sel = [0] * N


def powerset(idx, sum=0):
    if idx == N:
        if sum == 10:
            print(sel, " : ", end=" ")
            for i in range(N):
                if sel[i]:
                    print(arr[i], end=' ')
            print()
            return
        else:
            return


    # 해당자리를 뽑고 가고
    sel[idx] = 1
    tmp = sum + arr[idx]
    powerset(idx + 1, tmp)
    # ------------------------
    sel[idx] = 0
    powerset(idx + 1, sum)


powerset(0)