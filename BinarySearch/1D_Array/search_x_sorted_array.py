nums = [-1,0,3,5,9,12]
target = 5

def search_binary(nums: list[int], target: int) -> int:
    low = 0
    high = len(nums) - 1

    while low <= high:
        # Calculate the middle index
        mid = low + (high - low) // 2
        
        # Check if the middle element is the target
        if nums[mid] == target:
            return mid
        
        # If the target is greater, discard the left half
        elif nums[mid] < target:
            low = mid + 1
            
        # If the target is smaller, discard the right half
        else: # nums[mid] > target
            high = mid - 1
            
    return -1

nums = [-1,0,3,5,9,12]
target = 12
print(search_binary(nums, target))
        
    
# Brute Force

# index = -1

# for i in range(len(nums)):
#     if nums[i] == target:
#         index = i
#         break
        
# print(index)