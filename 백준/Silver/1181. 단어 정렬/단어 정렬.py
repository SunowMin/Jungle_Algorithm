# 1. 정렬 기준 함수 정의
def sort_key(word):
    # 길이 우선, 길이 같으면 사전순 정렬
    return (len(word), word)

# 2. 단어 개수 입력
n = int(input())

# 3. 중복 제거하면서 단어 입력받기
words = {input().strip() for _ in range(n)}

# 4. 정렬 (일반 함수 사용)
sorted_words = sorted(words, key=sort_key)

# 5. 출력
for word in sorted_words:
    print(word)
