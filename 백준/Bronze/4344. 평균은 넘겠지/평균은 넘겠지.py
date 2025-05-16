c = int(input())

for _ in range(c):
    input_data = list(map(int, input().split()))
    n = input_data[0]
    scores = input_data[1:]

    average = sum(scores) / len(scores)

    scoreSum = 0
    for score in scores:
        # 만약 평균보다 높은 사람이 있으면
        if score > average:
            scoreSum += 1
    percent = "%.3f%%" % ((scoreSum / len(scores))*100)
    print(percent)