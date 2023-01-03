def fib(n):
    if not n:
        return 0
    m = list(range(n+1))
    m[0] = 0
    m[1] = 1
    for i in range(2, n+1):
        m[i] = m[i-1] + m[i-2]
    return m[-1]

def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()