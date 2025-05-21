n = int(input())
arr = list(map(int, input().split()))

used = [False] * n         # 어떤 요소를 사용했는지 체크
current = []               # 현재 순열 조합
max_total = 0              # 결과 저장

def calculate_total(seq):
    total = 0
    for i in range(len(seq) - 1):
        total += abs(seq[i] - seq[i + 1])
    return total

def backtrack():
    global max_total

    # 1. 순열이 완성되었을 때
    if len(current) == n:
        total = calculate_total(current)
        max_total = max(max_total, total)
        return

    # 2. 순열 생성
    for i in range(n):
        if not used[i]:
            used[i] = True
            current.append(arr[i])
            backtrack()
            current.pop()
            used[i] = False

# 시작
backtrack()
print(max_total)
