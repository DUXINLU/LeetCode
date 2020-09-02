def yuefen(a, b):
    for i in range(2, min(a, b) + 1):
        print(a % i, b % i)
        while a % i == 0 and b % i == 0:
            a = int(a / i)
            b = int(b / i)
    return a, b


print(yuefen(2, 8))
