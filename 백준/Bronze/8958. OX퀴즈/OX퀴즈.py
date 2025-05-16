n = int(input())

for _ in range(n):
    a = input()
    sequence = 0
    score = 0
    for ch in a:
        if ch == 'O':
            sequence += 1
            score += sequence
        else:
            sequence = 0
    print(score)