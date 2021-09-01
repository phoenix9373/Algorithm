# C style

def push(item):
    global top
    if top > 100 - 1:
        return
    else:
        top += 1
        stack[top] = item

def pop():
    global top
    if top == -1:
        print("Stack is Empty!!")
        return
    else:
        result = stack[top]
        top -= 1
        return result

stack = [0] * 100 # 100개 크기로 만듦.
top = -1

push(1)
push(2)
push(3)