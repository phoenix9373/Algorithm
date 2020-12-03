# from math import ceil, log2
#
#
# def init_tree(node, s, e):
#     if s == e:
#         init_tree[node] = arr[s]
#     tree[node] = min(arr[s:e + 1])
#
#     mid = (s + e) // 2
#     init_tree(node*2, s, mid)
#     init_tree(node*2 + 1, mid + 1, e)
#
#
# while True:
#     tmp = input()
#     if len(tmp) == 1:
#         break
#
#     N = int(tmp[0])
#     arr = [[0]] + list(map(int, tmp[1:].split()))
#     size = ceil(log2(N))
#     tree = [0] * (size + 1)
#     init_tree(1, 0, N - 1)
#     print(tree)