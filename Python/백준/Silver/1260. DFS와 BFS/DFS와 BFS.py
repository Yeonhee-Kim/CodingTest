from collections import deque

# DFS 함수
def DFS_with_adj_list(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            # 방문할 수 있는 노드를 정렬하여 작은 번호부터 탐색
            stack += sorted(graph[n] - set(visited), reverse=True)  # 스택에 넣을 때 역순으로 정렬
    return visited

# BFS 함수
def BFS_with_adj_list(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            # 방문할 수 있는 노드를 정렬하여 작은 번호부터 탐색
            queue += sorted(graph[n] - set(visited))  # 큐에 넣을 때 정렬
    return visited

# 입력 받기
N, M, V = map(int, input().split())
graph = {i: set() for i in range(1, N + 1)}

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].add(v)
    graph[v].add(u)

# 결과 출력
dfs_result = DFS_with_adj_list(graph, V)
bfs_result = BFS_with_adj_list(graph, V)

print(" ".join(map(str, dfs_result)))
print(" ".join(map(str, bfs_result)))