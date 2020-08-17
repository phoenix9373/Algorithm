for c in range(1, int(input())+1):
    t = list(' '.join(input()).split())
    n = len(t)
    outer = '..#' + '...#'*(n-1) + '..'
    inner = '.#' + '.#'*(2*n-2) + '.#.'
    middle = f'#.{t[0]}' + ''.join([f'.#.{i}' for i in t[1:]]) + '.#'
    for i in range(5):
        if i in [0, 4]:
            print(outer)
        elif i in [1, 3]:
            print(inner)
        else:
            print(middle)