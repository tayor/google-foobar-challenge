def solution(n):
    n = int(n)
    operations = 0
    while n > 1:
        if n & 1:
            if n == 3 or n % 4 == 1: 
                n -= 1
            else:
                n += 1
        else:
            n >>= 1
        operations += 1
    return operations