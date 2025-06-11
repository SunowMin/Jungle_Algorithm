import sys
input = sys.stdin.readline

n = int(input())

# 계단 숫자 초기화
stairs = [0] * (n+3)

# 1번째 인덱스부터 저장
for i in range(1, n+1):
    stairs[i] = int(input())

# dp 배열을 초기화
dp = [0] * (n+3)
dp[1] = stairs[1]
dp[2] = stairs[1] + stairs[2]
dp[3] = max(stairs[1] + stairs[3], stairs[2]+stairs[3])

for i in range(4, n+1):
    dp[i] = max(dp[i-3]+stairs[i-1]+stairs[i],
                dp[i-2]+stairs[i])
    
print(dp[n])