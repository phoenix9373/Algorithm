import sys
n = int(sys.stdin.readline())
words = list(set([sys.stdin.readline().strip() for _ in range(n)]))

words = sorted(words, key=lambda x: (len(x), x))
print(*words, sep='\n')