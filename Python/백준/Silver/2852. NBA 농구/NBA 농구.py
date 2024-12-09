N = int(input())
total_time = 48 * 60 # 초단위로 변환

# 팀별 점수 및 이기고 있는 시간
team1_score = 0
team2_score = 0
team1_time = 0
team2_time = 0

prev_time = 0 # 직접 시간 초기화

for _ in range(N):
    team, time = input().split()
    team = int(team)
    M, S = map(int, time.split(':'))

    current_time = M * 60 + S

    # 현재 누가 이기고 있는지 확인하고 시간 누적
    if team1_score > team2_score:
        team1_time += current_time - prev_time
    elif team2_score > team1_score:
        team2_time += current_time - prev_time
    
    if team == 1:
        team1_score += 1
    else:
        team2_score += 1
    
    # 현재 시간을 직접 시간으로 업데이트
    prev_time = current_time

# 경기 종료 후 이긴 팀 (48분에서 차감해서 누적)
if team1_score > team2_score:
    team1_time += total_time - prev_time
elif team2_score > team1_score:
    team2_time += total_time - prev_time

# 초 단위를 MM:SS 형식으로 변환하여 출력
team1_minutes = team1_time // 60
team1_seconds = team1_time % 60
team2_minutes = team2_time // 60
team2_seconds = team2_time % 60

print(f"{team1_minutes:02}:{team1_seconds:02}")
print(f"{team2_minutes:02}:{team2_seconds:02}")

