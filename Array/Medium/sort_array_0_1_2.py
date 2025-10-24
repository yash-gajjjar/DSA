# Brute Force

nums = [1, 0, 2, 1, 0]

for i in range(len(nums)):  
    for j in range(i + 1, len(nums)):
        if nums[i] > nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
            
print(nums)
