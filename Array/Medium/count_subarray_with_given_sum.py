nums = [3, 1, 2, 4, 2]
k = 6

count = 0
for i in range(len(nums)):
    current_sum = 0
    for j in range(i, len(nums)):
        current_sum += nums[j]
        if current_sum == k:
            count += 1
            
print(count)