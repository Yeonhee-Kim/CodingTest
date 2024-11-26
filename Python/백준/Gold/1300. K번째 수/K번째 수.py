N = int(input())
k = int(input())

# 이진 탐색 범위 설정
start = 1
end = N * N
result = 0

while start <= end:
    mid = (start + end) // 2
    
    # mid 이하의 숫자 개수 계산
    count = 0
    for i in range(1, N + 1):
        count += min(N, mid // i)
    
    # mid 이하의 숫자 개수가 k 이상인 경우
    if count >= k:
        result = mid  # 현재 mid를 저장
        end = mid - 1  # 더 작은 값에서 탐색
    else:
        start = mid + 1  # 더 큰 값에서 탐색

print(result)