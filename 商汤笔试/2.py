def f(matrix):
    _ = []
    for i in matrix:
        _.append(min(i))
    i = _.index(min(_))
    j = matrix[i].index(min(matrix[i]))
    h, w = len(matrix), len(matrix[0])
    # print(i, j)

    queue = [[i, j]]
    k = matrix[i][j]
    dp = [[1 for x in range(w)] for y in range(h)]
    # print(dp)
    temp_pos = []
    temp_value = 9999999999
    while queue:
        i, j = queue.pop(0)
        print(i, j)
        if i > 0:
            if matrix[i - 1][j] != k:
                temp_pos.append([i - 1, j])
                temp_value = min(temp_value, matrix[i - 1][j])
        if i < h - 1:
            if matrix[i + 1][j] != k:
                temp_pos.append([i + 1, j])
                temp_value = min(temp_value, matrix[i + 1][j])
        if j > 0:
            if matrix[i][j - 1] != k:
                temp_pos.append([i, j - 1])
                temp_value = min(temp_value, matrix[i][j - 1])
        if j < w - 1:
            if matrix[i][j + 1] != k:
                temp_pos.append([i, j + 1])
                temp_value = min(temp_value, matrix[i][j + 1])

        for pos in temp_pos:
            if temp_value == matrix[pos[0]][pos[1]]:
                dp[pos[0]][pos[1]] = dp[i][j] + 1
                matrix[pos[0]][pos[1]] = k
                queue.append(pos)
                break
        temp_pos = []
        temp_value = 9999999999
    print(dp)


f([[9, 1, 4], [6, 2, 8], [5, 5, 7]])
