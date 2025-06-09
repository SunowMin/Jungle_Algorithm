import sys
input = sys.stdin.readline

expr = input()
# -기준으로 두 덩어리로 나누기
parts = expr.split("-")

first = 0
# + 기준으로 나눠서 다 더하기
for num in parts[0].split("+"):
    first += int(num)

rest = 0
for part in parts[1:]:
    subtotal = 0
    for num in part.split('+'):
        subtotal += int(num)
    rest += subtotal

print(first-rest)