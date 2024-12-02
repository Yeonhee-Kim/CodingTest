N, M = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range(M):
    a, b, c = map(int, input().split())

    if a == 1:
        arr[b-1] = c
    if a == 2: 
        for i in range(b-1, c):
            if arr[i] == 0:
                arr[i] = 1
            else:
                arr[i] = 0
    if a == 3:
        for i in range(b-1, c):
            arr[i] = 0
    if a == 4:
        for i in range(b-1, c):
            arr[i] = 1

print(' '.join(map(str, arr)))
