import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
q = deque()

for _ in range(n):
    str = input().split()
    s = str[0]
    
    if s == "push":
        q.append(str[1])
    elif s == "pop":
        print(q.popleft() if q else -1)
    elif s == "size":
        print(len(q))
    elif s == "empty":
        print(0 if q else 1)
    elif s == "front":
        print(q[0] if q else -1)
    elif s == "back":
        print(q[-1] if q else -1)