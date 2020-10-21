import sys

n = int(input())

nums = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
result = 0
def rgb(arr):
    min = 0
    for i in range(3):
        for j in range(3):
            if i != j:
                