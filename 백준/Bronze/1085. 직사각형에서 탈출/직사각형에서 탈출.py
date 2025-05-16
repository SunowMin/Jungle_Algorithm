x,y,w,h = map(int, input().split())

print(min(w-x, x-0, h-y, y-0))