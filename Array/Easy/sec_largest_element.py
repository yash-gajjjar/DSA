# def find_largest_element(nums):
#     max = nums[0]
#     second_max = 0
#     for i in range(len(nums)):
#         if nums[i] > max:
#             max = nums[i]
#     #print(max)

#     for i in range(len(nums)):
#         if nums[i] != max and nums[i] > second_max:
#             second_max = nums[i]   
               
#     return second_max

# b = find_largest_element(nums = [3,3,5,6,8,1])
# print(b)


def find_largest_element(nums):
    max = nums[0]
    second_max = 0
    
    for i in range(1, len(nums)):
        if nums[i] > max:
            second_max = max
            max = nums[i]
        elif nums[i] != max:
            if second_max is None or nums[i] > second_max:
                second_max = nums[i]
               
    return second_max

b = find_largest_element(nums = [3,3,5,6,8,1])
print(b)