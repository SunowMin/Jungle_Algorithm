import sys
input = sys.stdin.readline

n = int(input())
# stack 생성
stack = []

for _ in range(n):
    stick_height = int(input())
    stack.append(stick_height)

max_height = 0
cnt = 0

for i in range(len(stack)-1, -1, -1):
    if stack[i] > max_height:
        cnt += 1
        max_height = stack[i]

print(cnt)