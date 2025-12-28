nums= [3,5,8,15,19]
target = 9

def upper_bound(nums, x):
    low = 0
    high = len(nums)-1
    while low <= high:
        mid = low + (high - low) // 2
        
        if nums[mid] > x:
            ans = mid     
            high = mid - 1
        else:
            low = mid + 1
    return ans

nums= [3,5,8,15,19]
x = 9
print(upper_bound(nums, x))
            
        
        
    