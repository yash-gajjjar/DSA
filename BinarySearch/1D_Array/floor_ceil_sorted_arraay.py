def get_floor_and_ceil(nums, x):
    low = 0
    high = len(nums) - 1
    
    floor = -1
    ceil = -1
    
    while low <= high:
        mid = low + (high - low) // 2
        
        # Case 1: Exact match found
        if nums[mid] == x:
            return nums[mid], nums[mid]
        
        elif nums[mid] < x:
            low = mid + 1
            ceil = nums[mid]
            
        else:
            high = mid - 1
            floor = nums[mid]
            
    return ceil, floor

nums = [3, 4, 4, 7, 8, 10]

print(get_floor_and_ceil(nums, 5))
print(get_floor_and_ceil(nums, 8))