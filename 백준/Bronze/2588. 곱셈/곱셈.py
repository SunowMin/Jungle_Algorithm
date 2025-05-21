# 1. 두 수 입력받기
a = int(input())
b = int(input())

# 2. 두번째 입력받은 수를 세자리로 쪼개기
print(a*(b%10))
b1 = int(b/10)
# print(b1)
print(a*(b1%10))
b2 = int(b1/10)
print(a*b2)
print(a*b)