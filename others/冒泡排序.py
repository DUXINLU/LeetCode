def bubbleSort(num):
    for i in range(len(num)):
        for j in range(len(num) - i - 1):
            if num[j] > num[j + 1]:
                num[j], num[j + 1] = num[j + 1], num[j]
    return num


print(bubbleSort([6, 3, 7, 9, 0, 1, 4, 7]))
