t = int(input())


for _ in range(t):
    n = input()
    # vps인지 확인하는 변수 추가
    is_vps = 1
    stack = []

    for i in n:
        if i == "(":
            # (가 들어오면 스택에 push
            stack.append(i)
        else :
            # )가 들어오면 스택에서 pop
            if len(stack) == 0 :
                is_vps = 0
                break
            else:
                stack.pop()

    if is_vps == 1 and len(stack)==0:
        print("YES")
    else:
        print("NO")