import sys

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

# n = int(input())
# arr = [int(input()) for _ in range(n)]
# 빠른 입력
n = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(n)]

sorted_arr = merge_sort(arr)

# for num in sorted_arr:
#     print(num)
print("\n".join(map(str, sorted_arr)))
# # 빠른 출력
# sys.stdout.write("\n".join(map(str, sorted_arr) + "\n"))