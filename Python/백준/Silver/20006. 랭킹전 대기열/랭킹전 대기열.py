p, m =map(int, input().split()) # 플레이어 수, 방 정원 입력
rooms = [] 

for _ in range(p):
    l, n = input().split()
    l = int(l) # 레벨 int형으로 변환

    player = (l, n) # 플레이어 정보를 튜플로 저장

    # 1. 방 탐색해서 입장 가능한 방 찾기
    found_room = False
    for room in rooms:
        room_level = room[0][0] # 방의 기준 레벨 [(10, 'n')]
        if len(room) < m and room_level - 10 <= l <= room_level + 10:
            room.append(player)
            found_room = True
            break
    # 2. 입장 가능한 방이 없으면 새 방 생성
    if not found_room:
        rooms.append([player])

# 결과 출력
for room in rooms:
    if len(room) == m:
        print("Started!")
    else:
        print("Waiting!")
    for player in sorted(room, key=lambda x: x[1]):
        print(player[0], player[1])

    
