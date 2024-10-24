N = int(input())

# dp 테이블 초기화
dp = [0] * (N + 1)

# bottom-up 방식으로 dp 채우기
for i in range(2, N + 1):
    # 먼저 1을 뺀 경우를 저장
    dp[i] = dp[i - 1] + 1
    
    # 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    
    # 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

# 정답 출력
print(dp[N])