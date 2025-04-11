n = int(input())

def solution(str, stack):
    for i in str:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if len(stack) == 0:
                return("NO")
            stack.pop()
    if len(stack) == 0:
        return("YES")
    else:
        return("NO")


for _ in range(n):
    str = input()
    stack = []
    
    print(solution(str, stack))
    