K, N = map(int, input().split())
arr = []
for _ in range(K):
    i = int(input())
    arr.append(i)

start = 1
end = max(arr)

result = 0 # result 초기화
while start <= end:
    mid = (start + end) // 2
    cnt = 0

    for i in arr:
        cnt += i // mid
    
    if cnt >= N:
        result = mid
        start = mid + 1 # 최대 길이를 찾아야하는 거니까
    else:
        end = mid - 1

print(result)

