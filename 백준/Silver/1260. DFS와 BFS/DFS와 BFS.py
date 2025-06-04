import sys
input = sys.stdin.readline
from collections import deque

n, m, v = map(int, input().split())

# n*n 행렬 만들기
graph = [[0]*(n+1) for _ in range(n+1)]

# 그래프 정보 입력
for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

# 방문 여부 리스트
visited2 = [0] * (n+1)
visited = [0] * (n+1)

def bfs(v):
    queue = deque([v])
    visited2[v] = 1

    while queue:
        v = queue.popleft()
        print(v, end = " ")
        for i in range(1, n+1):
            if visited2[i] == 0 and graph[v][i] == 1:
                queue.append(i)
                visited2[i] = 1

def dfs_stack(v):
    stack = [v]

    while stack:
        v = stack.pop()
        if not visited[v] == 1:
            visited[v] = 1
            print(v, end=" ")
            # 역순으로 확인하여 작은 번호가 먼저 나오도록
            for i in range(n, 0, -1):
                if visited[i] == 0 and graph[v][i] == 1:
                    stack.append(i)

dfs_stack(v)
print()
bfs(v)