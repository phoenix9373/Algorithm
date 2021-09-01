# 그래프 자료구조
# 상호배타집합
# 1. 트리로 표현

tree = {}


def make_set(T, k):
    if T.get(k, 0) == 0:
        T[k] = k


def find_set(T, k):
    while T[k] != k:
        k = T[k]
    return k


def union(T, l, r):
    T[r] = l


make_set(tree, 'a')
make_set(tree, 'b')
union(tree, 'a', 'b')
make_set(tree, 'c')
union(tree, 'b', 'c')
make_set(tree, 'd')
union(tree, 'a', 'd')
print(tree)

print(find_set(tree, 'c'))