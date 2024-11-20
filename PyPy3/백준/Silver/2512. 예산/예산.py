N = int(input())
arr = list(map(int, input().split()))
M = int(input())

if sum(arr) <= M:
    print(max(arr))
else:
    total = 0
    result = 0
    cnt = 0
    start = min(arr)

    while total <= M:
        total = 0
        for i in arr:
            if i <= start:
                total += i
            else:
                total += start
        cnt += 1
        if total <= M:
            result = start
            start += 1
    
    if cnt == 1:
        print(M//N)
    else:
        print(start - 1)