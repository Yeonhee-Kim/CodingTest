N = int(input())
target = int(input())

# 초기화
arr = [[0] * N for _ in range(N)]
x,y = N//2, N//2 # 시작 위치(중앙)
arr[x][y] = 1

# 상 -> 우 -> 하 -> 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0,-1]

current = 2 # 제일 먼저 채울 숫자
target_pos = (x, y) # 타켓 좌표
step = 1 # 각 방향별 이동 횟수
direction = 0 # 처음 방향: 상 

while current <= N * N:
    for _ in range(step):
        if current > N * N:
            break
        x += dx[direction]
        y += dy[direction]
        arr[x][y] = current
        if current == target: # 타켓 좌표 저장
            target_pos = (x, y)
        current += 1

    direction = (direction + 1) % 4 # 방향 바꿔주고    
    if direction == 0 or direction == 2: # 상/하 일 때 이동 횟수를 1 증가해줌
         step += 1

# 출력
for a in arr:
     print(' '.join(map(str, a)))
print(target_pos[0]+1, target_pos[1]+1)
