import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

# 이분탐색하기 위해 받자마자 정렬
a.sort()

m = int(input())
b = list(map(int, input().split()))

def binarySearch(list, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    # 찾는 값이 mid면
    if list[mid] == target :
        return mid
    elif list[mid] > target:
        end = mid - 1
        return binarySearch(list, target, start, end)
    else:
        start = mid + 1
        return binarySearch(list, target, start, end)

for i in range(m):
    result = binarySearch(a, b[i], 0, n-1)

    if result is None:
        print("0")
    else:
        print("1")