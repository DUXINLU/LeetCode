import time
import random


def decorator(func):
    def wrapper(nums):
        start = time.time()
        func(nums)
        print('time:' + str(time.time() - start))

    return wrapper


def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list


@decorator
def findMax(nums):
    max_ = -2 ** 32

    for i in range(len(nums)):
        for j in range(i, len(nums)):
            sum_ = sum(nums[i:j + 1])
            if sum_ > max_:
                max_ = sum_
    print(max_)


@decorator
def findMaxPlus(nums):
    left, right = 0, len(nums) - 1
    max_ = -2 ** 32
    while left < right:
        if sum(nums[left:right + 1]) > max_:
            max_ = sum(nums[left:right + 1])
        if nums[left] < nums[right]:
            left += 1
        else:
            right -= 1
    print(max_)

@decorator
def findMaxDp(nums):
    for i in range(1,len(nums)):
        nums[i]=max(nums[i],nums[i-1]+nums[i])
    print(nums[-1])


nums = random_int_list(-10, 100, 100)
print(nums)
#findMax(nums)
findMaxPlus(nums)
findMaxDp(nums)
