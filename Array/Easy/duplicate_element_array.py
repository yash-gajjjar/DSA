def remove_duplicates(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                nums.pop(j)
                break
    return nums

nums = [1, 2, 3, 4, 5, 5, 6, 7, 7, 8]
result = remove_duplicates(nums)
print(result)