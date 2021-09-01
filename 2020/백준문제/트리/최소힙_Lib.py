# 최소힙만 지원
import heapq
heap = [7, 2, 5, 3, 4, 6]   # list
print(heap)
heapq.heapify(heap)
print(heap)

# 삽입
heapq.heappush(heap, 1)
print(heap)

# 삭제
while heap:
    print(heapq.heappop(heap), end=' ')
print()


# --------------------------------------v
# 최대힙

temp = [7, 2, 5, 3, 4, 6]
heap2 = []
for i in range(len(temp)):
    heapq.heappush(heap2, (-temp[i], temp[i])) # 아이템 2개를 -, +로 각각 넣는다.
heapq.heappush(heap2, (-1, 1)) # - 순으로 했기 때문에 +로 바꾸면 최대힙으로 바뀐다.
print(heap2)
while heap2:
    print(heapq.heappop(heap2)[1], end=' ')