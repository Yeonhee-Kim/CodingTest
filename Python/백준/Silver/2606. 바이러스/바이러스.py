from collections import deque

def bfs(graph, root):
    visited = []
    queue = deque([root])
    cnt = 0

    while queue:
        n = queue.popleft()

        if n not in visited:
            visited.append(n)
            cnt += 1
            queue += (graph[n] - set(visited))

    return cnt - 1

N = int(input())
M = int(input())
graph = {i: set() for i in range(1, N+1)}

for i in range(M):
    v, u = map(int, input().split())
    graph[v].add(u)
    graph[u].add(v)

print(bfs(graph, 1))