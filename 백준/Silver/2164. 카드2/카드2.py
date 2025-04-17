import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
card = deque()
card.extend(range(1, n+1))

while(True):
    if len(card) == 1:
        break
    card.popleft()
    card.append(card[0])
    card.popleft()

print(card[0])