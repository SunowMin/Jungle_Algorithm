import sys
sys.setrecursionlimit(10*6)
input=sys.stdin.readline

n,m = map(int,input().split())
board=[]

for _ in range(n):
    a=list(input().strip())
    board.append(a)

visited=[]

for _ in range(n):
    a=[False] * m
    visited.append(a)

def dfs(x,y):
    visited[x][y] = True
    current = board[x][y]

    if current == '-':
        ny = y+1
        if ny<m and not visited[x][ny] and board[x][ny] == '-':
            dfs(x, ny)

    if current == '|':
        nx = x+1
        if nx<n and not visited[nx][y] and board[nx][y] == '|':
            dfs(nx, y)


count = 0

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            dfs(i,j)
            count+=1
            
print(count)