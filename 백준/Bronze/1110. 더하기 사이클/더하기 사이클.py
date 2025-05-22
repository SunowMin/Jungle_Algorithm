n = int(input())
num = n
cnt = 0

while True:
    # 십의 자리
    a = num // 10 
    # 일의 자리
    b = num % 10
    # 새로운 수의 일의 자리
    c = (a+b)%10
    num = (b*10) + c

    cnt += 1

    # 종료 조건
    if n == num:
        break

print(cnt)