import sys
input = sys.stdin.readline

def color_check(x, y, size):
    global blue, white
    # 모든 칸을 돌면서 첫번째 칸의 색과 모두 같은지 확인
    # 첫 번째 칸의 색
    color = paper[x][y]
    all_same = True
    
    for i in range(x, x+size):
        for j in range(y, y+size):
            if paper[i][j] != color:
                all_same = False
                break
        if not all_same:
            break

    # 색이 섞여 있는 경우 4등분해서 재귀호출
    if not all_same:
        half = size // 2
        color_check(x,y,half)
        color_check(x, y+half, half)
        color_check(x+half, y, half)
        color_check(x+half, y+half, half)

    # 색이 섞여 있지 않은 경우
    else:
        # 파란색으로 차 있는 경우
        if color == 1:
            blue += 1
        else:
            white += 1

n = int(input())
paper = []
# 색종이 개수
blue = 0
white = 0

# 입력 받아서 리스트로 저장
for _ in range(n) :
    row = list(map(int, input().split()))
    paper.append(row)

# 종이가 모두 같은 색인지 확인
color_check(0,0,n)

print(white, blue, sep = "\n")