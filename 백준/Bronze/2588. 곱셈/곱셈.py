a = int(input())
b = int(input())

print(a*(b%10))
print(a*((b//10)%10))
print(a*((b//10//10)%10))
print(a*b)