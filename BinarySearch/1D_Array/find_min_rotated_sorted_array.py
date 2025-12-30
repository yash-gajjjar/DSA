def search_min_rotated_array(nums):
    low = 0
    high = len(nums) - 1
    ans = float('inf')

    while low <= high:
        mid = low + (high - low) // 2
        
        if nums[low] <= nums[high]:
            ans = min(ans, nums[low])
            break
        if nums[low] <= nums[mid]:
            ans = min(ans, nums[low])
            low = mid + 1
        else:
            ans = min(ans, nums[mid])
            high = mid - 1

    return ans

nums =  [4, 5, 6, 7, 0, 1, 2, 3]
print(search_min_rotated_array(nums))