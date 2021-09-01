def main():
    S = input()

    case = [S[-i:] for i in range(1, len(S) + 1)]

    print(*sorted(case), sep='\n')


if __name__ == '__main__':
    main()