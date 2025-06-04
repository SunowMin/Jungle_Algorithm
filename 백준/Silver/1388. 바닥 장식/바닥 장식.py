import sys

# 입력 받기
n, m = map(int, input().split())
floor = [list(input().strip()) for _ in range(n)]  # 바닥 정보 저장

# 방문 여부 체크용
visited = [[False]*m for _ in range(n)]

# DFS 함수 정의
def dfs(x, y, symbol):
    visited[x][y] = True  # 현재 칸 방문 처리

    # 연결된 방향으로만 이동
    if symbol == '-':
        # 오른쪽으로만 연결
        ny = y + 1
        if ny < m and not visited[x][ny] and floor[x][ny] == '-':
            dfs(x, ny, '-')

    elif symbol == '|':
        # 아래쪽으로만 연결
        nx = x + 1
        if nx < n and not visited[nx][y] and floor[nx][y] == '|':
            dfs(nx, y, '|')

# 판자 개수 세기
count = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            # 방문하지 않은 곳에서 새 판자 시작
            dfs(i, j, floor[i][j])
            count += 1

# 정답 출력
print(count)
