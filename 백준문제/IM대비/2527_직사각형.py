info = []
for _ in range(4):
    tmp = list(map(int, input().split()))
    info.append(sorted([tmp[:4], tmp[4:]]))


def answer(rects):
    rect1, rect2 = rects
        # 1. out
    if rect1[3] < rect2[1] or rect1[1] > rect2[3] or rect1[2] < rect2[0]:
        return 'd'
    if rect1[2] == rect2[0] and rect1[3] == rect2[1]:
        return 'c'
    if rect1[2] == rect2[0] and rect1[1] == rect2[3]:
        return 'c'
    if rect1[2] == rect2[0] and rect1[1] < rect2[1] < rect1[3]:
        return 'b'
    if rect1[3] == rect2[1] and rect1[0] < rect2[0] < rect1[2]:
        return 'b'
    if rect1[1] == rect2[3] and rect1[0] < rect2[0] < rect1[2]:
        return 'b'

    return 'a'


for rects in info:
    res = answer(rects)
    print(res)