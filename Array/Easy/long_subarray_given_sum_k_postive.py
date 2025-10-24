# Brute Force Approach

def longest_subarray_with_sum_k(nums, k):
    count = 0
    
    for i in range(len(nums)):
        current_sum = 0
        for j in range(i, len(nums)):
            current_sum += nums[j]
            if current_sum == k:
                count = max(count, j - i + 1)
                break
            elif current_sum > k:
                break
    if count == 0:
        print("No subarray with sum found")

    return count

nums = [-1, 1, 1]
k = 1
result = longest_subarray_with_sum_k(nums, k)
print(result)


# Optimized Approach using Sliding Window

def longest_subarray_non_negative(nums, k):
    left = 0
    current_sum = 0
    max_length = 0
    
    for right in range(len(nums)):
        current_sum += nums[right]
        
        # Contract the window if the sum exceeds K
        while current_sum > k and left <= right:
            current_sum -= nums[left]
            left += 1
            
        # Check for the target sum (if k=0, it's possible the sum is K after contraction)
        if current_sum == k:
            max_length = max(max_length, right - left + 1)
            
    return max_length