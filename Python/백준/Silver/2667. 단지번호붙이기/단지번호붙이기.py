# 입력 값을 받아서, 2차원 배열로 저장
N = int(input()) # 지도의 N 크기
board = [list(map(int,input())) for _ in range(N)] # 지도

# 방문한 집을 표시하기 위한 배열
visited = [[False] * N for _ in range(N)]

# 방향
dx = [-1, 1, 0, 0] # 상, 하
dy = [0, 0, -1, 1] # 좌, 우

# 단지 저장 리스트
complex_list = []

def dfs(x, y):
  visited[x][y] = True # 현재 위치 방문 처리
  count = 1 # 현재 집을 포함하므로 count 1로 시작

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and board[nx][ny] == 1: 
      count += dfs(nx, ny) # 재귀적으로 연결된 집을 탐색하면서 count 증가
  
  return count

# 지도 탐색하면서 단지별로 DFS 실행
for i in range(N):
  for j in range(N):
    if board[i][j] == 1 and not visited[i][j]:
      complex_list.append(dfs(i, j)) # dfs 실행 후 단지 크기 추가

# 결과 출력
complex_list.sort() # 단지 크기 오름차순 정렬
print(len(complex_list)) # 총 단지 수 출력
for count in complex_list:
  print(count)
  
  