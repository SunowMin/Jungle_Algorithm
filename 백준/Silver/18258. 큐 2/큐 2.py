import sys
from collections import deque
input = sys.stdin.readline

# collections모듈의 deque 클래스를 이용해서 queue라는 이름의 빈 덱(deque) 객체 생성
queue = deque()
n = int(input())

for _ in range(n):
    # 입력 받기 (입력이 한번에 한개가 들어올지, 두개가 들어올지 모르니까 map으로 입력받기)
    com = input().split()

    if com[0] == "push":
        queue.append(com[-1])

    elif com[0] == "pop":
        # queue에 요소가 있다면
        if queue:
            print(queue.popleft())
        # 리스트가 비어있다면
        else :
            print(-1)

    elif com[0] == "size":
        print(len(queue))

    elif com[0] == "empty":
        # 비어있으면
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    elif com[0] == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    else :
        if queue :
            print(queue[-1])
        else:
            print(-1)