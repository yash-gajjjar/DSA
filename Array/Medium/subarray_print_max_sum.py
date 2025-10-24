nums =  [2, 3, 5, -2, 7, -4]

sum = nums[0]
new = []    

for i in range(len(nums)):
    current_sum = 0
    for j in range(i, len(nums)):
        current_sum += nums[j]
        sum = max(sum, current_sum)
        if sum == current_sum:
            new = nums[i:j+1]

print(f"Subarray with maximum sum {sum}: {new}")