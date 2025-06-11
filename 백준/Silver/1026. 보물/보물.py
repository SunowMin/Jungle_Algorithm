import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = 0

for _ in range(n):
    result += min(a) * max(b)
    a.remove(min(a))
    b.remove(max(b))

print(result)