def find_first(nums, target):
    low, high = 0, len(nums) - 1
    first = -1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            first = mid
            high = mid - 1 
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return first


def find_last(nums, target):
    low, high = 0, len(nums) - 1
    last = -1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            last = mid
            low = mid + 1  
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return last

def search_range(nums, target):

    first = find_first(nums, target)
    
    if first == -1:
        return [-1, -1]
    
    last = find_last(nums, target)
    
    return [first, last]

nums = [5, 7, 7, 8, 8, 10]
print(search_range(nums, 8)) 
print(search_range(nums, 6)) 