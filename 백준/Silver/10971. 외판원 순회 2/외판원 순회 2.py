import sys


sys.setrecursionlimit(10**6)


def make_graph():
    return [list(map(int, input().split())) for _ in range(N)]


def recur(start, current, count, cost):
    global min_cost
    
    
    if count == N and graph[current][start] != 0 :
        min_cost = min(min_cost, cost + graph[current][start])
        return
    
    for i in range(N):
        if visited[i] == 0 and graph[current][i] != 0:
            visited[i] = 1
            recur(start, i, count+1, cost + graph[current][i])
            visited[i] = 0
        
        


input = sys.stdin.readline


N = int(input())
graph = make_graph()
visited = [0]*N

min_cost = float('inf')

visited[0] = 1
recur(0,0,1,0)
print(min_cost)