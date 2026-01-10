import math

def calculate_total_hours(nums, k):
    total_hours = 0
    for pile in nums:
        total_hours += math.ceil(pile / k)
    return total_hours

def min_eating_speed(nums, h):
    low = 1
    high = max(nums)
    ans = high
    
    while low <= high:
        mid = low + (high - low) // 2
        
        total_time = calculate_total_hours(nums, mid)
        
        if total_time <= h:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
            
    return ans

nums = [7, 15, 6, 3]
h = 8
print(min_eating_speed(nums, h))




