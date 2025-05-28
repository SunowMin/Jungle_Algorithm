import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    stack = list(input().split())

    print("Case #"+(str)(i+1)+": ", end = "")
    for j in range(len(stack)):
        print(stack.pop(), end=" ")
    print()