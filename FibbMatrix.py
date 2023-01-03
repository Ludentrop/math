def main():
    n = int(input())
    print(fib(n))



def pow(x, n, I, mult):
    """
    Returns x^n, n > 0
    I is an identity matrix that multiplies with mult
    """
    if n == 0:
        return I
    elif n == 1:
        return x
    else:
        y = pow(x, n // 2, I, mult)
        y = mult(y, y)
        if n % 2:
            y = mult(x, y)
        return y


def identity_matrix(n):
    """
    Returns an identity matrix n*n
    """
    r = list(range(n))
    return [[1 if i == j else 0 for i in r] for j in r]


def matrix_multiply(A, B):
    BT = list(zip(*B))
    return [[sum(a * b
                 for a, b in zip(row_a, col_b))
            for col_b in BT]
            for row_a in A]


def fib(n):
    F = pow([[1, 1], [1, 0]], n, identity_matrix(2), matrix_multiply)
    return F[0][1]


if __name__ == '__main__':
    main()
