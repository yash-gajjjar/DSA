def missingNumber(nums):
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)

#M2

nums = [2,0,1,4]
n = len(nums)
sum_num = 0

sum = n * (n + 1) // 2

for i in range(n):
  sum_num += nums[i]

missing_num = sum - sum_num
print(missing_num)