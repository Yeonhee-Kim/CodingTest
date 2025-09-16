from collections import deque
def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    
    while progresses:
        # 1. 하루 경과: 모든 작업 진도 업데이트
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        
        # 2. 맨 앞 작업이 완료되었으면 계속 배포
        count = 0 
        while progresses and progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            count += 1
        
        # 3. 오늘 배포된 게 있으면 answer에 기록
        if count > 0:
            answer.append(count)    
    
    return answer