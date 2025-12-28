def search_insert_position(nums, target):
    low = 0
    high = len(nums) - 1
    ans = len(nums)
    
    while low <= high:
        
        mid = low + (high-low)//2
        
        if nums[mid] == target:
            return mid
            
        elif nums[mid] < target:
            low = mid + 1
            
        else: 
            ans = mid
            high = mid - 1

    return ans 

nums = [1, 3, 5, 6]
target = 2
print(search_insert_position(nums, target))