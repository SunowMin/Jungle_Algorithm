# 입력 받기
N = int(input())           # 첫 번째 줄: 수의 개수
numbers = []               # 숫자들을 저장할 리스트

for _ in range(N):
    num = int(input())
    numbers.append(num)    # 리스트에 숫자 추가

# 정렬하기
numbers.sort()

# 출력하기
for num in numbers:
    print(num)