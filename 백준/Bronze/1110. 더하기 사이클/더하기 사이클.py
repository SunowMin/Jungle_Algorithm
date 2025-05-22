def sum_cycle(n):
    global cycle

    # a는 10의 자리 수
    # b는 1의 자리 수
    # c는 a+b
    a = n[0]
    b = n[-1]
    c = str(int(a) + int(b))

    # 새로운 수 생성
    s = b+c[-1]
    cycle += 1

    if s == z:
        print(cycle)
    else :
        sum_cycle(s)

n = input()
z = n
cycle = 0

# 주어진 수가 10보다 작다면 앞에 0을 붙여 두자리로 만들기
# if int(n) == 0:
#     print("1")
# elif int(n) < 10:
#     n = '0' + str(n)
#     z = str(n)
#     sum_cycle(str(n))
# else:
#     n=n
#     sum_cycle(n)

if int(n) < 10:
    n = '0' + str(n)
    z = str(n)
    sum_cycle(str(n))
else:
    n=n
    sum_cycle(n)
