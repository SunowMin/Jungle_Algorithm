import sys
input = sys.stdin.readline
from collections import deque

# 큐 생성
queue = deque()

n = int(input())

for i in range(1, n+1):
    queue.append(i)

while len(queue) > 1:
    # 제일 위에 있는 카드 버리기
    queue.popleft()
    # 그 다음 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮김
    queue.append(queue.popleft())

print(queue[0])