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

    # 두 리스트를 정렬하면서 병합
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 남은 요소 추가
    result.extend(left[i:])
    result.extend(right[j:])

    return result

# 입력 받기
n = int(input())
arr = [int(input()) for _ in range(n)]

# 정렬
sorted_arr = merge_sort(arr)

# 출력
for num in sorted_arr:
    print(num)
