# Brute Force 

nums =  [2, 3, 5, -2, 7, -4]

sum = nums[0]

for i in range(len(nums)):
    current_sum = 0
    for j in range(i, len(nums)):
        current_sum += nums[j]
        sum = max(sum, current_sum)
        
print(sum)

# Optimized Approach - Kadane's Algorithm

def max_subarray_sum(nums):
    # Handle the edge case of an empty list
    if not nums:
        return 0
    
    # Initialize both the maximum sum found so far (max_so_far)
    # and the maximum sum ending at the current position (current_max)
    # to the first element of the array.
    max_so_far = nums[0]
    current_max = nums[0]
    
    # Iterate through the rest of the elements
    for i in range(1, len(nums)):
        # current_max is either the current element itself, 
        # or the current element added to the previous current_max.
        # This decides whether to start a new subarray or continue the current one.
        current_max = max(nums[i], current_max + nums[i])
        
        # max_so_far is the maximum of the overall max and the current_max.
        max_so_far = max(max_so_far, current_max)
        
    return max_so_far

# Test Cases
nums1 = [2, 3, 5, -2, 7, -4]
nums2 = [-2, -3, -7, -2, -10, -4]

print(f"Input: {nums1}, Output: {max_subarray_sum(nums1)}")
print(f"Input: {nums2}, Output: {max_subarray_sum(nums2)}")