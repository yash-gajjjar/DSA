nums = [1, 1, 0, 1, 0, 0, 1] 
k = 3

for i in range(len(nums)):
    for j in range(i + 1, len(nums) + 1):
        subarray = nums[i:j]
        if sum(subarray) == k:
            print(subarray)
