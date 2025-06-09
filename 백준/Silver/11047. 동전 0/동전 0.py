import sys
input = sys.stdin.readline

# 동전종류n, k원 만들기 
n, k = map(int, input().split())

# 동전 종류 입력받기
coins = [int(input()) for _ in range(n)]
total = 0

for i in range(n-1, -1, -1):
    if k >= 0:
        # 몫
        count = k // coins[i]
        # 나머지
        k %= coins[i]
        # 동전 개수
        total += count

print(total)