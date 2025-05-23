import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))

count = 0

def dfs(idx, current_sum):
    global count
    if idx == N:
        if current_sum == S:
            count += 1
        return

# 전체 수열의 조합(=모든 부분수열)을 구하는 부분분
    # 현재 원소 선택
    dfs(idx + 1, current_sum + arr[idx])

    # 현재 원소 선택하지 않음
    dfs(idx + 1, current_sum)

dfs(0, 0)

# 공집합의 경우는 제외 (합이 0인 경우 포함되므로 빼줘야 함)
if S == 0:
    count -= 1

print(count)
