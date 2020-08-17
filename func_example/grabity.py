# from random import*
# def build_data():
#     for i in range(0, 9):
#         data[i]=randint(0, 9)

# data=[0]*10
# build_data()

data = [7, 4, 2, 0, 0, 6, 0, 7, 0]
max_val = 0
for i in range(len(data)):
    cnt = 0

    for j in range(i+1, len(data)):
        if data[i] > data[j]:
            cnt += 1
    
    if max_val<cnt:
        max_val = cnt

print(max_val)
