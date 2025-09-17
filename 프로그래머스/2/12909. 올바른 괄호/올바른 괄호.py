def solution(s):
    answer = True
    result = []
    for i in range(len(s)):
            if s[i] == "(":
                result.append(s[i])
            else:
                if not result:
                    return False
                result.pop()
    
    
    if not result:
        answer = True
    else:
        answer = False
        
    return answer

