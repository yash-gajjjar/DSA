nums = [1, 1, 2, 1, 1] 
k = 3 # number of odd numbers in subarray

for i in range(len(nums)):
    for j in range(i + 1, len(nums) + 1):
        subarray = nums[i:j]
        odd_count = sum(1 for x in subarray if x % 2 != 0)
        if odd_count == k:
            print(subarray)