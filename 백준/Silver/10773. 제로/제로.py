k = int(input())
stack = []

for _ in range(k):
    money = int(input())

    if money == 0:
        stack.pop()
    else:
        stack.append(money)

print(sum(stack))