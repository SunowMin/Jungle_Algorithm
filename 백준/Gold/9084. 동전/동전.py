import sys
input = sys.stdin.readline

# 테스트케이스 개수:t
t = int(input())

for _ in range(t):
    # 동전의 가지 수:n
    n = int(input())
    # n가지 동전 금액 (오름차순)
    coins = list(map(int, input().split()))
    # 목표 금액
    m = int(input())

    dp = [0] * (m+1)
    # 아무 동전도 사용하지 않고 0을 만드는 방법은 1가지 (아무것도 선택 안 함)
    dp[0] = 1

    for coin in coins :
        for amount in range(coin, m+1):
            dp[amount] += dp[amount-coin]

    print(dp[m])