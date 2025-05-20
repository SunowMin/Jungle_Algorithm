import sys

input = sys.stdin.readline
counts = [0] * 10001

n = int(input())
for _ in range(n):
    num = int(input())
    counts[num] += 1

for i in range(1, 10001):
    for _ in range(counts[i]):
        sys.stdout.write(f"{i}\n")
