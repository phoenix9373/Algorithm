import sys


def make_except_idx():
    except_idx = []
    # idx = 0. 나머지 1부터 8까지 2개 제거.
    for i in range(1, N - 1):
        for j in range(i + 1, N):
            except_idx.append([i, j])
    # idx = 1. 나머지 2부터 8까지 1개 제거.
    for i in range(2, N):
        except_idx.append([0, i])
    # idx = 2. 나머지 3부터 8까지 0개 제거.
    except_idx.append([0, 1])
    return except_idx


N = 9
arr = sorted([int(sys.stdin.readline()) for _ in range(N)])
exceptions = make_except_idx()

for idxs in exceptions:
    tmp = [i for idx, i in enumerate(arr) if idx not in idxs]
    if sum(tmp) == 100:
        print(*tmp, sep='\n')
        break