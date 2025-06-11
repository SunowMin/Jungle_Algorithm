import sys
input = sys.stdin.readline

n = int(input())

a = []
for _ in range(n):
    a.append(int(input()))

result = []
for _ in range(n):
    m = min(a)
    result.append((m * len(a)))
    a.remove(m)

# print(min(a)*n)
print(max(result))