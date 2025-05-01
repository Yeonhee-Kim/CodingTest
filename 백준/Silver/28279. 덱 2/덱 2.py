import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
mydep = deque()

for _ in range(n):
    s = input().split()
    if s[0] == "1":
        mydep.appendleft(int(s[1]))
    elif s[0] == "2":
        mydep.append(int(s[1]))
    elif s[0] == "3":
        if len(mydep) == 0:
            print(-1)
        else:
            print(mydep.popleft())
    elif s[0] == "4":
        if len(mydep) == 0:
            print(-1)
        else:
            print(mydep.pop())
    elif s[0] == "5":
        print(len(mydep))
    elif s[0] == "6":
        if len(mydep) == 0:
            print(1)
        else:
            print(0)
    elif s[0] == "7":
        if len(mydep) == 0:
            print(-1)
        else:
            print(mydep[0])
    elif s[0] == "8":
        if len(mydep) == 0:
            print(-1)
        else:
            print(mydep[-1])