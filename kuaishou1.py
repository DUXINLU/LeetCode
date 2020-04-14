'''
import sys
input = None
data = ''
for line in sys.stdin:
    input = line.strip()'''
data = ''
input = '1*2+(3+3)))((('
ans = 0
for i in input:
    if i == '(' or i == ')' or i == '[' or i == ']':
        data += i

l = []

for i in data:
    if i == '(':
        l.append(i)
        continue
    if i == ')':
        if not l:
            l.append(i)
            continue
        if l[-1] == '(':
            l.pop()
            ans += 1
            continue
        else:
            l.append(i)
            continue
    if i == '[':
        l.append(i)
        continue
    if i == ']':
        if not l:
            l.append(i)
            continue
        if l[-1] == '[':
            l.pop()
            ans += 1
            continue
        else:
            l.append(i)
            continue

print(ans, l.count('(') + l.count('['), l.count(')') + l.count(']'))
