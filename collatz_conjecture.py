def collatz(n):
    if n in [0, 1]:
        print([0, 1][n])
    else:
        step = 1
        while n != 1:
            if n % 2 == 0:
                n /= 2
                print(f'{step}: {n:.0f}')
                step += 1
                continue
            else:
                n = n * 3 + 1
                print(f'{step}: {n:.0f}')
                step += 1
