N, M = map(int, input().split())
arr = list(map(int, input().split()))

# 초기 값 세팅
start = max(arr)
end = sum(arr)

while start <= end:
    mid = (start + end) // 2 # 블루레이 크기 기준!!
    total = 0 # 블루레이 크기 총합
    count = 1 # 블루레이 개수

    for i in arr:
        if total + i > mid: # 블루레이 크기 넘어가면
            count += 1 # 다음 블루레이에 저장
            total = 0 # 다음 블루레이 total 값 초기화하고 다시 더해줌
        total += i # 하나의 블루레이에 녹화 영상 저장
    
    if count <= M: # 블루레이 개수가 맞으면
        result = mid # 일단 mid값 저장해두고
        end = mid - 1 # 혹시 더 작은 값이 있을 수도 있으니 탐색해봄
    else: # 블루레이 개수 너무 많으면
        start = mid + 1

print(result)


