def solution(s):
    answer = -1
    stack = []
    
    for char in s:
            if not stack or stack[-1] != char:
                stack.append(char)
            else:
                stack.pop()
    
    if stack:
        answer = 0
    else:
        answer = 1
        
    return answer