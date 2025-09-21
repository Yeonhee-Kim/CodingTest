N = int(input())
stack = []
total = 0
for _ in range(N):
    num = int(input())
    if num != 0:
        stack.append(num)
        total += num
    elif num == 0:
        re = stack.pop()
        total -= re

print(total)