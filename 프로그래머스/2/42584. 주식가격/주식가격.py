from collections import deque

def solution(prices):
    answer = []
    queue = deque(prices)
    
    while queue:
        target = queue.popleft()
        cnt = 0
        for i in queue:
            if target > i:
                cnt += 1
                break
            cnt += 1
        answer.append(cnt)
    
    return answer