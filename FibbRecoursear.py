def fib(n):
	if n in [0, 1]:
		return [0, 1][n]
	return fib(n-1) + fib(n-2)


def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()
