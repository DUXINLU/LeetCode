import sys


def f():
    path = list(sys.stdin.readline().strip())

    x_stack, y_stack = [], []

    path_set = [[x_stack, y_stack]]

    for i in path:
        print(i)
        print(x_stack, y_stack)
        if i == 'N':
            if x_stack:
                if x_stack[-1] == 'S':
                    x_stack.pop()
            else:
                x_stack.append('N')
        if i == 'S':
            if x_stack:
                if x_stack[-1] == 'N':
                    x_stack.pop()
            else:
                x_stack.append('S')
        if i == 'E':
            if y_stack:
                if y_stack[-1] == 'W':
                    y_stack.pop()
            else:
                y_stack.append('E')
        if i == 'W':
            if y_stack:
                if y_stack[-1] == 'E':
                    y_stack.pop()
            else:
                y_stack.append('W')
        if [x_stack, y_stack] in path_set:
            print(True)
            return
        else:
            path_set.append([x_stack, y_stack])

    print(False)


try:
    f()
except:
    print(False)
