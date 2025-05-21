n = int(input())

for _ in range(n):
    s,r = input().split()
    s = int(s)

    for ch in r:
        print(ch*s, end="")
    print()