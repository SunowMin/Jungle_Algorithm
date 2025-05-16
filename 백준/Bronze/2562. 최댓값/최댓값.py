# nums = list(map(int, input().split()))
nums = [int(input()) for _ in range(9)]

# 최대값 구하기
max_value = max(nums)
max_index = nums.index(max_value) + 1

print(f"{max_value}\n{max_index}")