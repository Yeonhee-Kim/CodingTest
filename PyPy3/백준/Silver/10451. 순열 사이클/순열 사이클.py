from collections import deque

def bfs(graph, N):
    visited = []
    cnt = 0
    for i in range(1, N+1):
        if i in visited:
            continue
        else:
            queue = deque([i])

            while queue:
                n = queue.popleft()
                if n not in visited:
                    visited.append(n)
                    queue.append(graph[n])
            cnt += 1
    
    return cnt

T = int(input())
graph = []

for _ in range(T):
    N = int(input())
    n = list(map(int, input().split()))
    graph = [0] + n
    print(bfs(graph, N))
