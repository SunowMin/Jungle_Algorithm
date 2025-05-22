def queen(row):
    global answer
    if row == n:        # n번까지 위치 확인 했다면 경우의 수 추가
        answer += 1
        return
    for col in range(n):
        if check_col[col] or check_upward[row + col] or check_downward[row - col + n - 1]:      # 같은 열에 존재하거나 같은 대각선에 존재하면 다음 열 위치
            continue
        # 해당 모든 경우의 수를 찾기 위해 백트레킹 사용
        check_col[col] = True
        check_upward[row + col] = True
        check_downward[row - col + n - 1] = True
        queen(row + 1)
        check_col[col] = False
        check_upward[row + col] = False
        check_downward[row - col + n - 1] = False
n = int(input())
answer = 0
check_col = [False] * n     # 같은 열에 위치하는지 체크
check_upward = [False] * (2*n)      # 대각선에 위치하는지 체크 ( 2*n은 대각선의 행의 개수)
check_downward = [False] * (2*n)        # 대각선에 위치하는지 체크
queen(0)        # 인덱스 0번부터 시작
print(answer)