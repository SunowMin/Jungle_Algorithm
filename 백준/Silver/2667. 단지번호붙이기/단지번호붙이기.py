import sys
from collections import deque
input = sys.stdin.readline

# 지도의 크기
n = int(input())
# 단지 번호 저장
vil = [list(input().strip()) for _ in range(n)]
# 방문 여부 확인
visited = [[0]*n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
     q = deque()
     q.append((x,y))
     visited[x][y] = 1
     cnt = 1 # 시작 집 포함

     while q :
          x,y = q.popleft()
          for i in range(4) :
               nx = x + dx[i]
               ny = y + dy[i]
               if 0 <= nx < n and 0 <= ny < n:
                if vil[nx][ny] == '1' and not visited[nx][ny] :
                        visited[nx][ny] = 1
                        cnt += 1
                        q.append((nx,ny))
     return cnt

result = []

for i in range(n):
    for j in range(n):
        # 집이 있고 방문하지 않았다면
        if vil[i][j] == '1' and visited[i][j] == 0:
                count = bfs(i,j)
                result.append(count)

print(len(result))
for r in sorted(result):
     print(r)