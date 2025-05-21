import sys

# 재귀 최대 깊이를 늘려줌 (파이썬의 재귀 최대 깊이 기본 설정 : 1,000회)
sys.setrecursionlimit(10**6)

# DFS 함수: 재귀로 모든 도시 순열을 탐색
# start → 시작 도시 번호 (처음 고정됨)
# current → 현재 도시 번호
# count → 현재까지 방문한 도시 수
# cost → 현재까지 이동한 총 비용
def recur(start, current, count, cost):
    global min_cost   
    
    # 모든 도시를 다 방문했을 때 (count==N)
    # 현재 도시에서 출발도시(start)로 돌아올 수 있다면 (graph[current][start] != 0)
    if count == N and graph[current][start] != 0 :
        # 총 비용에 마지막 복귀 비용을 더한 후 → min_cost 갱신
        min_cost = min(min_cost, cost + graph[current][start])
        return
    
    for i in range(N):
        # 아직 방문하지 않은 도시(visited[i] == 0
        # 현재 도시에서 갈 수 있다면 (graph[current][i] != 0), 한 번 갔던 도시는 못가니까
        if visited[i] == 0 and graph[current][i] != 0:
            # 방문 표시하고 → 다음 도시로 이동 (recur() 호출)
            visited[i] = 1
            recur(start, i, count+1, cost + graph[current][i])
            # 호출 끝나면 되돌아가기 (백트래킹) → 방문 표시 해제
            visited[i] = 0

input = sys.stdin.readline

N = int(input())
# 비용 행렬
graph = [list(map(int, input().split())) for _ in range(N)]
# 방문 체크 배열
visited = [0]*N
# 최소 비용 추적용 변수
# float('inf') : '실수형 양의 무한대'를 의미
min_cost = float('inf')

# 도시 0을 출발 도시로 고정
visited[0] = 1
recur(0,0,1,0)
print(min_cost)