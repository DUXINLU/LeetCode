def yuefen(a, b):
    for i in range(2, min(a, b) + 1):
        while a % i == 0 and b % i == 0:
            a = int(a / i)
            b = int(b / i)
    return a, b


def f():
    import sys

    n1, op, n2 = sys.stdin.readline().strip().split()

    fenzi1, fenmu1 = n1.split('/')
    fenzi1, fenmu1 = int(fenzi1), int(fenmu1)

    fenzi2, fenmu2 = n2.split('/')
    fenzi2, fenmu2 = int(fenzi2), int(fenmu2)

    if fenzi1 == 0 or fenzi2 == 0:
        print(0)
        return
    fenzi, fenmu = 0, 0
    if op == '+':
        fenzi = fenzi1 * fenmu2 + fenzi2 * fenmu1
        fenmu = fenmu1 * fenmu2
        print('%s/%s' % yuefen(fenzi, fenmu))
        return

    if op == '-':
        fenzi = fenzi1 * fenmu2 - fenzi2 * fenmu1
        fenmu = fenmu1 * fenmu2
        if fenzi == 0:
            print(0)
        if fenzi < 0:
            print('-%s/%s' % yuefen(-fenzi, fenmu))
        if fenzi > 0:
            print('%s/%s' % yuefen(fenzi, fenmu))
        return

    if op == '*':
        fenzi = fenzi1 * fenzi2
        fenmu = fenmu1 * fenmu2
        print('%s/%s' % yuefen(fenzi, fenmu))
        return

    if op == '/':
        fenzi = fenzi1 * fenmu2
        fenmu = fenmu1 * fenzi2
        print('%s/%s' % yuefen(fenzi, fenmu))
        return


f()
