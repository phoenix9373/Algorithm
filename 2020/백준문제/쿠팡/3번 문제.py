# set 활용.

def solution(k, score):

    diff_list = [0] + [abs(score[i + 1] - score[i]) for i in range(len(score) - 1)]
    unique_diff_list = list(set(diff_list))
    checked_list = [i for i in unique_diff_list if diff_list.count(i) >= k]

    arr = [1] * len(score)
    for k in checked_list:
        for idx, d in enumerate(diff_list):
            if idx != 0 and k == d:
                arr[idx - 1] = 0
                arr[idx] = 0

    ans = sum(arr)
    return ans

print(solution(2, [1300000000,700000000,668239490,618239490,568239490,568239486,518239486,157658638,157658634,100000000,100]))