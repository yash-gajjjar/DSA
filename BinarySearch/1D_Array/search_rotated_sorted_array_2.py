def search_in_rotated_array(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            return True
        if nums[low] <= nums[mid]:
             if nums[low] <= target < nums[mid]:
                high = mid - 1 
             else: 
                low = mid + 1
        else:
             if nums[mid] <= target < nums[high]:
                low = mid + 1 
             else: 
                low = mid + 1
            
    return False

nums = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6]
target = 10
print(search_in_rotated_array(nums, target))