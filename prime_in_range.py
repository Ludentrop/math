def prime_in_range(n: int) -> 'generator':
    '''
    INPUT: integer
    OUTPUT: generator
    DESCRIPTION: Return a generator of prime numbers in range n
    '''

    def is_prime(n):
        flag = True

        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                flag = False
        if flag and n > 1:
            return True
        return False

    for i in range(2, n):
        if is_prime(i):
            yield i



if __name__ == '__main__':
    print(list(prime_in_range(int(input()))))
