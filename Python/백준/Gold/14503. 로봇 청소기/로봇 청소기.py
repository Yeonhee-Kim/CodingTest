N, M = map(int, input().split())
r,c,d = map(int, input().split())

board = [0 for _ in range(N)]

for i in range(N):
    board[i] = list(map(int, input().split()))

# 북 동 남 서 
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
count = 0
while True:
    if board[r][c] == 0: # 현재 좌표가 청소가 안 돼있으면
        board[r][c] = 2 # 청소해줌 (1: 벽, 0: 노 청소, 2: 청소 완료)
        count += 1
    
    cleand = False
    # 네 방향 탐색
    for _ in range(4):
        d = (d + 3) % 4 # 왼쪽 회전
        nr = r + dx[d]
        nc = c + dy[d]

        if board[nr][nc] == 0: # 청소 안 돼있으면
            r, c = nr, nc # 이동해줌
            cleand = True
            break # 이동했으면 다른 방향 탐색 중단
    # 네 방향 다 청소 돼있거나, 벽인 경우
    if cleand == False:
        back_dir = (d + 2) % 4
        br = r + dx[back_dir]
        bc = c + dy[back_dir]

        if board[br][bc] != 1: # 벽이 아니면
            r,c = br, bc # 후진
        else: # 후진 불가능하면 종료
            break

print(count)


