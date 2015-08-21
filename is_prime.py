def is_prime(x):
    if x < 0:
        return False
    if x==0 or x == 1:
        return False
    if x == 2:
        return True
    if x%2 == 0:
        return False
    for n in range(2,x):
        if x%n == 0:
            return False
        elif x%n!=0 and n!=x-1:
            continue
        else:
            return True
