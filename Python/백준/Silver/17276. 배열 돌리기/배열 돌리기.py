def rotate_matrix(matrix, N, d):
    degree = (d//45) % 8 # 8번 회전 = 45도
    if degree < 0: # 음수면 양수로 변환해줌 ex) -1 == 7
        degree += 8
    
    for _ in range(degree):
        new_matrix = [[0] * N for i in range(N)]  # 새로운 2차원 배열

        # 1. 주 대각선 -> 가운데 열
        for i in range(N):
            new_matrix[i][N//2] = matrix[i][i]
        
        # 2. 가운데 열 -> 부 대각선
        for i in range(N):
            new_matrix[i][N-1-i] = matrix[i][N//2]
        
        # 3. 부 대각선 -> 가운데 행
        for i in range(N):
            new_matrix[N//2][N-1-i] = matrix[i][N-1-i]
        
        # 4. 가운데 행 -> 주 대각선
        for i in range(N):
            new_matrix[i][i] = matrix[N//2][i]
        
         # 5. 나머지 원소 그대로 복사
        for i in range(N):
            for j in range(N):
                # 주 대각선, 부 대각선, 가운데 열, 가운데 행에 속하지 않는 경우
                if i != j and i != N - 1 - j and i != N // 2 and j != N // 2:
                    new_matrix[i][j] = matrix[i][j]
        
        matrix = new_matrix 
        
    return matrix

T = int(input())

for _ in range(T):
    N, d = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    result = rotate_matrix(matrix, N, d)

    for j in result:
        print(' '.join(map(str, j)))
