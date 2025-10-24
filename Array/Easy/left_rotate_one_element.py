#Method 1
def left_rotate_one_element(nums):
    for i in range(len(nums)-1):
        nums[i], nums[i+1] = nums[i+1], nums[i]
    return nums
    
result = left_rotate_one_element(nums = [1, 2, 3, 4, 5])
print(result)

#Method 2
def left_rotate_one_element(nums):
    first_element = nums[0]

    for i in range(len(nums)-1):
        nums[i] = nums[i+1]
    nums[-1] = first_element
    return nums 

result = left_rotate_one_element(nums = [1, 2, 3, 4, 5, 6])
print(result)

