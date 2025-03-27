n = int(input())
num = list(map(int, input().split()))

max = num[0]
min = num[0]
for i in num:
    if max < i:
        max = i
    if min > i:
        min = i

print(min, max)