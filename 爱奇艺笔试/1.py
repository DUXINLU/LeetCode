import sys

n = int(sys.stdin.readline().strip())

tens = 0
twos = 0
fives = 0

for i in range(1, n + 1):
    while i % 10 == 0:
        i = i // 10
        tens += 1
    while i % 5 == 0:
        i = i // 5
        fives += 1
    while i % 2 == 0:
        i = i // 2
        twos += 1

print(tens + min(fives, twos))
