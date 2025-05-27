import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
queue = deque()

for i in range(1, n+1):
    # 큐에 1~n까지의 값 입력
    queue.append(i)

li = []
# 길이가 1이 될때까지
while (len(queue) >= 1):
    # queue.rotate(-2)
    queue.rotate(-(k-1))
    li.append(queue.popleft())

print('<' + ', '.join(map(str, li)) + '>')


    