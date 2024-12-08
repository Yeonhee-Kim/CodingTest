s = input()
s2 = s.upper()

arr = [0 for _ in range(26)]

for i in s2:
    idx = ord(i) - 65
    arr[idx] += 1

max_val = max(arr)  # 최대값 계산
if arr.count(max_val) > 1:  # 최대값이 중복되는지 확인
    print("?")
else:
    result = arr.index(max_val) + 65
    print(chr(result))