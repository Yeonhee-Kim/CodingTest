n = int(input()) 

factor = 2  # 첫 번째 소수
while factor * factor <= n:  
    while n % factor == 0:  
        print(factor)
        n //= factor
    factor += 1

if n > 1:  
    print(n)