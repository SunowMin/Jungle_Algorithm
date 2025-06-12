n = int(input())
cnt_5 = n // 5
rest = n % 5

while cnt_5 >= 0:
    # 만약 남은 거스름돈이 2로 나누어진다면,
    if rest % 2 == 0:
        # 2원의 개수 추가
        cnt_2 = rest // 2
        print(cnt_5 + cnt_2)
        break
    # 나누어 지지 않는다면, 5원의 개수 -1
    cnt_5 -= 1
    # 5원을 뺀만큼, 남은 거스름돈에 +5
    rest += 5
else:
    print(-1)