N = int(input())
arr = list(map(int, input().split()))
M = int(input())

start = 0
end = max(arr)
result = 0

while start <= end:
    mid = (start + end) // 2
    total = sum(min(mid, x) for x in arr)

    if total <= M:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)