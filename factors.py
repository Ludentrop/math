def nat_mul(n):
    nat_nums = []
    count = 2
    while n != 1:
        if str(n / count)[-1] != '0':
            count += 1
            continue
        else:
            n /= count
            nat_nums.append(count)
    print(*nat_nums)
