# nums = [1, 2, 1, 2, 3]
# k = 2

nums = [1, 2, 1, 3, 4]
k = 3  
n = len(nums)
subarray = []
count = 0

for i in range(n):
    for j in range(i, n):
        current_subarray = nums[i : j + 1]
        if len(set(current_subarray)) == k:
            count += 1
            
print(count)
  