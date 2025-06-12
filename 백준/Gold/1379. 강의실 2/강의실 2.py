import sys, heapq

input = sys.stdin.readline
N = int(input())

lectures = []
for _ in range(N):
    num, start, end = map(int, input().split())
    lectures.append((start, end, num))

# 시작 시간 기준으로 정렬
lectures.sort()

heap = []  # 종료 시간, 강의실 번호
room_count = 0  # 현재까지 사용한 강의실 개수
room_assignment = [0] * (N + 1)  # 강의 별로 배정된 강의실 번호 저장

available_rooms = []  # 재사용 가능한 강의실 번호 저장용 heap

for start, end, num in lectures:
    # 현재 회의 시작 시각보다 먼저 끝난 회의는 회의실 재사용 가능
    while heap and heap[0][0] <= start:
        _, room = heapq.heappop(heap)
        heapq.heappush(available_rooms, room)

    # 재사용 가능한 회의실이 있다면 사용
    if available_rooms:
        room = heapq.heappop(available_rooms)
    else:
        room_count += 1
        room = room_count  # 새 강의실 번호 할당

    # 현재 회의 종료시간, 강의실 번호를 heap에 추가
    heapq.heappush(heap, (end, room))
    room_assignment[num] = room

print(room_count)
for i in range(1, N + 1):
    print(room_assignment[i])