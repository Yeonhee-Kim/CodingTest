from collections import deque

def solution(bridge_length, weight, truck_weights):
    cnt = 0
    bridge = deque([0] * bridge_length) # 다리 위 상태 (앞이 출구)
    cur_weight = 0 # 현재 다리 총 하중
    waiting = deque(truck_weights) # 대기 트럭
    
    while bridge:
        cnt += 1
        # 1) 한 칸 전진: 출구 쪽 트럭/빈칸이 내려감
        out = bridge.popleft()
        cur_weight -= out
        
        # 2) 새 트럭 진입 (대기가 남아 있고, 무게 여유가 있으면)
        if waiting:
            if cur_weight + waiting[0] <= weight:
                t = waiting.popleft()
                bridge.append(t)
                cur_weight += t
            else:
                bridge.append(0)
        
        # 대기가 비었으면 더 이상 append 안 함 => while 종료

    return cnt