# 그래프 자료구조
# 상호배타집합
# 1. 트리로 표현
class Dijkstra:

    def __init__(self):
        self.tree = {}

    def make_set(self, element):
        if self.tree.get(element, 0) == 0:
            self.tree[element] = element

    def union(self, left, right):
        while self.tree[left] != left:
            left = self.tree[left]
        while self.tree[right] != right:
            right = self.tree[right]
        self.tree[right] = left

    def find_set(self, element):
        return self.tree[element]


test = Dijkstra()
test.make_set('c')
test.make_set('d')
test.union('c', 'd')
test.make_set('e')
test.make_set('f')
test.union('d', 'f')
print(test.find_set('d'))
print(test.find_set('f'))