import sys
from collections import deque

input = sys.stdin.readline
N, K = map(int, input().split())
Q = deque(range(1, N + 1))

# 요세푸스 순열
res = []
while len(Q) != 0:
    for _ in range(K-1):
        # K-1번째 노드까지 Q 맨 뒤로 이동
        Q.append(Q.popleft())
    # K번째 노드 삭제 후 결과 배열에 추가 
    res.append(str(Q.popleft()))

print('<'+', '.join(res)+'>')