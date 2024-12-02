import heapq
import sys
input = sys.stdin.readline

N = int(input())
arr = []

for _ in range(N):
    x = int(input())
    if x != 0:
        # 튜플 형태로 리스트에 저장 => 자동 정렬
        heapq.heappush(arr, (abs(x), x))
    else:
        if arr:
            print(heapq.heappop(arr)[1]) # 원본 출력
        else: # 비어있으면
            print(0)