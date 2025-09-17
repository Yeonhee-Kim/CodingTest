from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque(priorities)
    result = deque(i for i in range(len(priorities)))# 0 1 2 3
    
    target = priorities[location] # 2
    
    while True:
        num = queue[0]
        result_num = result.popleft()
        if num != max(queue):
            queue.popleft()
            queue.append(num)
            result.append(result_num)
        else:
            if num == target and result_num == location:
                queue.popleft()
                answer += 1
                break
            else:
                queue.popleft()
                answer += 1
    
    return answer