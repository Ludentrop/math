def pascal(n):
    row = [1]
    y = [0]
    for x in range(n):
        print(' ' * int((n-x)//2)*2, row)
        row = [l + r for l, r in zip(row + y, y + row)]
pascal(int(input('> ')))