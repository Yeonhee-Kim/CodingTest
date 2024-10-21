from collections import deque

def bfs(graph):
  cnt = 0 # 연결 요소 개수 저장
  visited = [] # 방문한 노드 기록

  for i in range(1, N+1):
    if i not in visited: # 방문하지 않은 노드라면 BFS 실행
      queue = deque([i])
    else: 
      continue # 이미 방문 했으면 다음 노드로 넘어감
  
    while queue: # 큐가 빌 때까지
      n = queue.popleft()

      if n not in visited: # 방문하지 않은 노드일 경우
        visited.append(n) # 방문한 것으로 기록
        # 현재 노드와 연결된 노드 중 아직 방문하지 않은 노드를 큐에 추가
        queue += graph[n] - set(visited)
    
    cnt = cnt + 1 # 하나의 연결 요소를 찾아서 +1

  return cnt

N, M = map(int, input().split())
graph = {i: set() for i in range(1, N+1)} # 각 노드에 대한 인접 리스트를 빈 집합으로 초기화

for _ in range(M):
  u, v = map(int, input().split())
  graph[u].add(v) # u 노드에 v 노드를 연결
  graph[v].add(u) # v 노드에도 u 노드를 연결 (양방향 그래프)

print(bfs(graph)) 