import sys

l1 = int(sys.stdin.readline().strip())
arr1 = list(map(int, list(sys.stdin.readline().strip().split(' '))))
l2 = int(sys.stdin.readline().strip())
arr2 = list(map(int, list(sys.stdin.readline().strip().split(' '))))

ans = []

for i in arr1:
    if i in arr2:
        ans.append(i)
        arr2.remove(i)

ans.sort(reverse=True)

print(' '.join(list(map(str, ans))))
