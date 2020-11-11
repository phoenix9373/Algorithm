import sys

sys.stdin = open("test.txt", "r")
for c in range(1, int(input()) + 1):
    nums = [list(map(int, input().split())) for _ in range(9)]
    def find(lst):
        for num in lst:
            if len(set(num)) < 9:
                return 0
        
        for i in range(len(lst)):
            temp = [lst[j][i] for j in range(len(lst))]
            if len(set(temp)) < 9:
                return 0
        
        X = [0, 1, 2]
        Y = [0, 1, 2]
        for x in X:
            for y in Y:
                temp = []
                for i in X:
                    for j in Y:
                        temp.append(lst[3*x+i][3*y+j])
                if len(set(temp)) < 9:
                    return 0
        return 1
    result = find(nums)
    print(f'#{c} {result}')