L, C = map(int, input().split())
enc = list(input().split())
enc.sort()
ans = []

def is_valid():  # 모음과 자음의 개수를 검사하는 함수
    vowels = {'a', 'e', 'i', 'o', 'u'}
    vowel_count = sum(1 for char in ans if char in vowels)
    consonant_count = len(ans) - vowel_count
    return vowel_count >= 1 and consonant_count >= 2

def back(start):
    if len(ans) == L: # 배열 길이 확인
        if is_valid():
            print("".join(ans))
    for i in range(start, len(enc)):
        if enc[i] not in ans:
            ans.append(enc[i])
            back(i+1)
            ans.pop()

back(0)