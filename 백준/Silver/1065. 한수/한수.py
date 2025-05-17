num = int(input()) # 135

hansu = 0
for i in range(1, num+1): # 1~135까지 반복
    num_list = list(map(int, str(i))) # 1~135까지 배열 생성
    if i < 100: 
        hansu += 1
    elif num_list[0] - num_list[1] == num_list[1]-num_list[2]:
        hansu += 1

print(hansu)