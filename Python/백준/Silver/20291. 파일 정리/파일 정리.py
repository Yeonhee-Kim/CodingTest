T = int(input())
file = {}

for _ in range(T):
    s = input().split('.')
    file_name = s[1]

    if file_name in file:
        file[file_name] += 1
    else:
        file[file_name] = 1

for ext, cnt in sorted(file.items()):
    print(f"{ext} {cnt}")
        