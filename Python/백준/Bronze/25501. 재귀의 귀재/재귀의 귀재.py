def recursion(s, cnt):
    cnt += 1
    if len(s) <= 1:  # 종료 조건: 문자열이 빈 문자열이거나 길이 1인 경우
        return isPalindrome(1, cnt)
    if s[0] != s[-1]:  # 첫 글자와 마지막 글자가 다르면 팰린드롬이 아님
        return isPalindrome(0, cnt)
    return recursion(s[1:-1], cnt)  # 양 끝을 제외한 부분에 대해 다시 확인

def isPalindrome(n, cnt):
    if n == 0:
        print(0, cnt)
    if n == 1:
        print(1, cnt)

T = int(input())
for _ in range(T):
    s = input()
    recursion(s, 0)