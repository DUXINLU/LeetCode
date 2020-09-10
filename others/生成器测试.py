def generator():
    while True:
        answer = (yield)
        if answer:
            if '0' in answer:
                print('false')
            if '1' in answer:
                print('true')


g = generator()
next(g)
g.send('1')
