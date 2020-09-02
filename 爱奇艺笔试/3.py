import sys

s = list(sys.stdin.readline().strip())
stack = []

for i in s:
    if not stack:
        stack.append(i)
        continue
    if i == '{' or i == '(' or i == '[':
        stack.append(i)
        continue
    if i == ')':
        if stack[-1] == '(':
            stack.pop()
        else:
            stack.append(i)
        continue
    if i == ']':
        if stack[-1] == '[':
            stack.pop()
        else:
            stack.append(i)
        continue
    if i == '}':
        if stack[-1] == '{':
            stack.pop()
        else:
            stack.append(i)
        continue

print(stack == [])
