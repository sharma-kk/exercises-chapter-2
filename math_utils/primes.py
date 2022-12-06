def isprime(n):
    """prime number indentifier (insert a natural number to check)"""
    import math
    a = int(math.sqrt(n))
    if n == 1:
        return False
    elif n ==2:
        return True
    elif n==3:
        return True
    else:
        for i in range(2, n+1):
            if n%i == 0:
                break
        if i == n:
            return True
        else:
            return False

