num = input()  
original_num = int(num)  
if original_num < 10:  # 한 자리 숫자일 경우 앞에 0을 붙임
    num = '0' + num

current = num  # 현재 숫자
cnt = 0  

while True:
    cnt += 1
    digit_sum = int(current[0]) + int(current[1])
    # 새로운 숫자 만들기
    current = current[-1] + str(digit_sum % 10)
    
    # 숫자가 원래 숫자로 돌아왔는지 확인
    if int(current) == original_num:
        break

print(cnt)