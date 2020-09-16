def binarySearch(array, num, l, r):
    if r >= l:
        mid = int(l + (r - l) / 2)

        if array[mid] == num:
            return mid

        if array[mid] > num:
            return binarySearch(array, num, l, mid - 1)
        else:
            return binarySearch(array, num, mid + 1, r)
    else:
        return -1


print(binarySearch([1, 4, 5, 8, 10, 20, 49], 5, 0, 6))
