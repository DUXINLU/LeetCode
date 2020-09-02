def decorator(func):
    def wrapper():
        func()
        print('decorator done.')

    return wrapper


@decorator
def f():
    print('this is f.')


f()
