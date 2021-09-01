# isEmpty(), isFull()
# 공백상태, 포화상태 검사
# 공백상태: front = rear
# 포화상태: 삽입할 다음

Q = [0] * 4
front, rear = -1, -1
SIZE = 4


def enQueue(item):
    global rear
    if (rear + 1) % SIZE == front: # Full
        print("Queue Full")
    else:
        rear = (rear + 1) % SIZE
        Q[rear] = item


def deQueue():
    global front
    if front == rear:
        print("Queue Empty")
    else:
        front = (front + 1) % SIZE
        return Q[front]


def Qpeek(): # 삭제 시 가장 앞에 있는 값 조회.
    if front == rear:
        print("Queue Empty")
    else:
        return Q[(front + 1) % SIZE]


def is_empty():
    if front == rear:
        print("Queue Empty")
    else:
        pass

# 비었을 때와 구분하기 위해 원형 큐는 항상 한 칸을 비워놓는다.
def is_full():
    if front == (rear + 1) % SIZE:
        print("Queue is full")



enQueue(1)
enQueue(2)
enQueue(3)
print(Qpeek())
print(deQueue())
print(deQueue())
print(deQueue())