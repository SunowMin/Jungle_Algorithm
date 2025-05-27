import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
# deque 클래스의 queue 객체 생성
queue = deque()

for i in range(1,n+1):
    # 리스트에 값 추가
    queue.append(i)

for i in range(n):
    # 카드가 한 장 남으면
    if len(queue) == 1:
        print(queue.pop())
    else:
        # 제일 위에 있는 카드 버리기-popleft
        queue.popleft()

        # 맨 위에 있던 카드 버리기-pop, 그 다음 위에 있는 카드 값을 맨 아래에 추가-appendleft
        temp = queue.popleft()
        queue.append(temp)