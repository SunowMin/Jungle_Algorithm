n = int(input())
words = {input().strip() for _ in range(n)}  # set으로 중복 제거

# 정렬: (1) 길이 오름차순 → (2) 사전순
sorted_words = sorted(words, key=lambda x: (len(x), x))

for word in sorted_words:
    print(word)
