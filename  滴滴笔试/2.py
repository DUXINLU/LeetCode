def f(n):
    fibbo = [1, 1]
    if n < 3:
        return [1 for i in range(n)]
    for i in range(2, n):
        fibbo.append(fibbo[i - 2] + fibbo[i - 1])
    return fibbo


class Spiral:
    def __init__(self, N, fibbo):
        self.matrix = [[None for i in range(N)] for j in range(N)]
        self.row = 0
        self.col = 0
        self.max_row = N
        self.mark = 0
        self.fibbo = fibbo

    # 获取数组的运动方向
    def direction(self, mark):
        around = [
            [self.row, self.col + 1],  # 向右
            [self.row + 1, self.col],  # 向下
            [self.row, self.col - 1],  # 向左
            [self.row - 1, self.col]  # 向上
        ]
        return around[mark % 4]

    # 根据当前位置，获取下一个位置
    # 如果是边界更换方向
    # 如果下一个元素已经有了同样也要更换方向
    def next(self):
        # 获取下一个位置
        i = self.direction(mark=self.mark)
        # 判断是不是赋值和越界，如果没有，赋值螺旋数组上的数组位置值
        if -1 not in i and self.max_row not in i:
            if self.matrix[i[0]][i[1]] is None:
                # 赋值self.row = i[0],self.col = i[1]
                self.row, self.col = i
                return None
        # 更换方向
        self.mark += 1
        return self.next()

    def solution(self):
        for i in range(1, self.max_row ** 2 + 1):
            # 行列赋值
            # print(self.fibbo)
            self.matrix[self.row][self.col] = self.fibbo.pop()
            # 结束
            if i == self.max_row ** 2:
                break
            self.next()
        # 打印结果
        for r in self.matrix:
            for c in r:
                print('{0:^{1}}'.format(c, 1), end=' ')
            print('')


import sys

n = int(sys.stdin.readline().strip())
s = Spiral(n, f(n * n))
s.solution()
