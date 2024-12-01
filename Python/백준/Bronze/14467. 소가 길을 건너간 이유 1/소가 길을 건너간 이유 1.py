T = int(input())
N_arr = [False for _ in range(100)]
D_arr = [0 for _ in range(100)]

cnt = 0
for _ in range(T):
    N, direction = map(int, input().split())

    if N_arr[N] == False:
        N_arr[N] = True
        D_arr[N] = direction
    else:
        if D_arr[N] != direction:
            cnt += 1
            D_arr[N] = direction

print(cnt)