import math
n = input()

# 수가 들어왔는지 확인하는 리스트 생성 (0으로 채워진)
check = [0] * 10

# 122 입력
for ch in n:
    if(int(ch) == 6 or int(ch) == 9):
        check[6] += 0.5
    else:
        check[int(ch)] += 1

print(math.ceil(max(check)))