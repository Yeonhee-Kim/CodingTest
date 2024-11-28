H, W = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0

for i in range(1, W-1):
    left_max = max(arr[:i])
    rigt_max = max(arr[i+1:])

    compare = min(left_max, rigt_max)

    if arr[i] < compare:
        ans += (compare - arr[i])

print(ans)

