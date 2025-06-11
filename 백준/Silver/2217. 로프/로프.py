import sys
input = sys.stdin.readline

n = int(input())

a = []
for _ in range(n):
    a.append(int(input()))

# 10 15 20
a.sort()

result = []
for _ in range(n):
    result.append((a[0] * len(a)))
    a.remove(a[0])

# print(min(a)*n)
print(max(result))