# 스택과 마찬가지로 삽입, 삭제가 제한적인 자료구조
# 큐의 앞에서는 삭제만, 큐의 뒤에서는 삽입만.
# 선입선출구조

# 초기상태: front == rear == -1
# 공백상태: front == rear
# 포화상태: rear == n - 1
# 잘못된 포화인식: 연산을 반복 중, 앞부분이 비어있음에도 포화라고 나옴.
# 해결방법: 머리속으로 원형으로 Q가 이루어져있다고 생각. % 연산을 활용하여 rear가 n-1이고 앞부분이 비었을 때 (rear + 1) % n 에 item 넣음.

Q = [0] * 100
n = len(Q)
front, rear = -1, -1


def create_queue(n): # n 크기의 빈 Q를 생성.
    global front, rear
    front, rear = -1, -1
    return [0] * n


def en_queue(item): # 삽입
    global rear
    if len(Q) - 1 == rear:
        print("Queue Full")
    else:
        rear += 1
        Q[rear] = item


def de_queue():
    global front
    if front == rear:
        print("Queue Empty")
    else:
        front += 1
        print(Q[front])


def is_empty():
    # global front, rear => 전역변수를 변경하는 작업이 아니면 필요 없음.
    if front == rear:
        return True
    else:
        return False


def is_full():
    if rear == n - 1:
        return True
    else:
        return False