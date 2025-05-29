import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.sort()

m = int(input())
b = list(map(int, input().split()))


def binarySearch(start, end, target):
    mid = (start+end)//2
    if start>end:
        return 0

    if target == a[mid] :
        return 1
    
    elif target > a[mid]:
        start = mid + 1
        return binarySearch(start, end, target)
        
    else:
        end = mid - 1
        return binarySearch(start, end, target)

for i in range(m):
    result = binarySearch(0, n-1, b[i])
    print(result)