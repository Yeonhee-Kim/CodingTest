N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input())
target = list(map(int, input().split()))

def binary_search(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:

        mid = (start + end) // 2

        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0

for i in target:
    print(binary_search(A, i))