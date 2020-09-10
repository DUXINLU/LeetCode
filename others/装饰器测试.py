def decorator(func):
    def wrapper(*args):
        print('decorator done.')
        print(sum(args))

    return wrapper


@decorator
def f(a, b):
    print('this is f.')


f(1, 2)
