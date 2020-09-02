import sys

n, k = sys.stdin.readline().strip().split()
# n, k = map(int, [n, k])

# l = map(int, list(sys.stdin.readline().strip()))
l = sys.stdin.readline().split()

l.remove(k)

print(' '.join(l))
