def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    p = arr[len(arr) // 2]
    L = [i for i in arr if i < p]
    R = [i for i in arr if i > p]
    E = [i for i in arr if i == p]
    return quick_sort(L) + E + quick_sort(R)


for tc in range(1, int(input()) + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    res = quick_sort(nums)
    print('#{} {}'.format(tc, res[N//2]))