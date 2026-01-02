def find_rotation_count(nums):
    low = 0
    high = len(nums) - 1
    ans = float('inf')
    index = -1
    
    while low <= high:
        mid = low + (high - low) // 2
        
        if nums[low] <= nums[high]:
            if nums[low] < ans:
                index = low
                ans = nums[low]
            break
        
        if nums[low] <= nums[mid]:
            if nums[low] < ans:
                index = low
                ans = nums[low]
            low = mid + 1
            
        else:
            if nums[mid] <= ans:
                index = mid
                ans = nums[mid]
            high = mid - 1
            
    return index

nums = [4, 5, 6, 7, 0, 1, 2, 3]
print(find_rotation_count(nums))