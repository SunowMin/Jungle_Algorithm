# 전체 종이 가로,세로 
width, height  = map(int, input().split())
num_cuts = int(input())

horizontal_cuts = [0, height]
vertical_cuts = [0, width]

# 자를 구간 입력 (가로:0/세로:1, 점선번호)
for _ in range(num_cuts):
    cut_type, cut_position = map(int, input().split())
    if cut_type == 0:
        horizontal_cuts.append(cut_position)
    else:
        vertical_cuts.append(cut_position)

horizontal_cuts.sort()
vertical_cuts.sort()

max_h = 0
max_v = 0
for i in range(len(horizontal_cuts) - 1):
    # 수평 자른 간격
    current_gap = horizontal_cuts[i+1] - horizontal_cuts[i]
    if(current_gap > max_h):
        max_h = current_gap
for i in range(len(vertical_cuts) - 1):
    # 수직 자른 간격
    current_gap = vertical_cuts[i+1] - vertical_cuts[i]
    if(current_gap > max_v):
        max_v = current_gap

print(max_h*max_v)