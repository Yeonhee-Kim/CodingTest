N = int(input())

def p(N):
    if N == 0:
        return 0
    if N == 1:
        return 1
    return p(N-1) + p(N-2)

print(p(N))