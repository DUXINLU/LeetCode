import sys

n = int(sys.stdin.readline().strip())
jump_high = sys.stdin.readline().strip().split()
jump_far = sys.stdin.readline().strip().split()

jump_high_index = jump_high.index('X')
jump_far_index = jump_far.index('X')

better_num, worse_num = 0, 0

for i in jump_high[:jump_high_index]:
    if i in jump_far[:jump_far_index]:
        better_num += 1

for i in jump_high[jump_high_index + 1:]:
    if i in jump_far[jump_far_index + 1:]:
        worse_num += 1

print('%d %d' % (better_num + 1, n - worse_num))
