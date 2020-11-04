# Python style stack
# 스택을 어떻게 구현하는지 알아두자!!

stack = []

def push(item):
    stack.append(item) # 가장 마지막 index에 item을 추가.

def pop():
    # stack이 비었을 때의 조건.
    if len(stack) == 0:
        print("Stack is empty.")
        return
    else:
        return stack.pop() # list의 pop 함수.

push(1)
push(2)
push(3)

print(pop())
print(pop())
print(pop())