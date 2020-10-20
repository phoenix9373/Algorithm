import random
random.seed(1) # 시드 고정.

n = int(input()) # 학생 수.
card = [random.sample(range(1, 14), 4) for _ in range(n)] # 학생 수만큼 카드 뽑기.

minValue = 0 # 최솟값을 저장할 변수.