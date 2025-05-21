c = int(input())

for _ in range(c):
    avg = 0
    cnt = 0

    a = list(map(int, input().split()))
    n = a[0]
    scores = a[1:]

    avg = sum(scores)/n

    for ch in scores:
        if ch > avg:
            cnt += 1

    # print((cnt / len(scores)) * 100)
    # print(f"{percent:.3f}%")
    print(f"{(cnt / len(scores)) * 100:.3f}%")
    # percent = "%.3f%%" % ((sum / len(li))*100)