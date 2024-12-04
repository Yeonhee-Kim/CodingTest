N = int(input())
arr = list(map(int, input().split()))
new_arr = [0 for i in range(N)]

for i in range(N):
    cnt = 0
    for j in range(N):
        if cnt == arr[i] and new_arr[j] == 0:
            new_arr[j] = i + 1
            break
        if new_arr[j] == 0:
            cnt += 1

print(' '.join(map(str, new_arr)))