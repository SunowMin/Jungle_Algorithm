import sys
from collections import deque
input = sys.stdin.readline

# n학생수, m키를비교한횟수
n,m = map(int, input().split())
# 인접 리스트(그래프) 생성 : 학생별로 뒤에 서야 하는 학생들 저장
graph = [[] for _ in range(n+1)]
# 각 학생의 indegree(자신 앞에 서야 하는 학생 수) 초기화
indegree = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    # a->b(a보다 b가 뒤에 서야 함)
    graph[a].append(b)
    # 간선을 읽으면서 indgree 배열 채우기
    indegree[b] += 1

# indegree가 0인 정점을 저장할 큐 생성
queue = deque()

# indegree가 0인 학생들을 먼저 넣기(앞에 아무도 없는 학생)
for i in range(1, n+1):
    if indegree[i] == 0:
        queue.append(i)

# 결과 리스트 : 줄 세운 순서를 저장
result = []

# 위상정렬 시작
while queue:
    # 큐에서 학생 하나 꺼냄
    student = queue.popleft()
    # 결과에 추가(줄 세우기)
    result.append(student)

    # 꺼낸 학생 뒤에 서야 하는 학생들에 대해 indegree 줄이기
    for next_student in graph[student]:
        indegree[next_student] -= 1
        if indegree[next_student] == 0:
            # indegree가 0이 되면 큐에 추가
            queue.append(next_student)

print(*result)