nums = [100, 4, 200, 1, 3, 2, 5, 9]

for i in range(len(nums)):
    for j in range(len(nums) - 1):
        if nums[i] < nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
            
print(nums)

max_length = 0

for i in range(len(nums)):
    current_length = 1
    for j in range(i + 1, len(nums)):
        if nums[j] == nums[j - 1]:
            continue
        elif nums[j] == nums[j - 1] + 1:
            current_length += 1
        else:
            break
        
    max_length = max(max_length, current_length)

print(max_length)