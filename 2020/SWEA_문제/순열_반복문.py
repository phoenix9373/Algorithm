for a in range(3):
    for b in range(3):
        if a == b:
            continue
        for c in range(3):
            if a == c or c == b:
                print(a, b, c)