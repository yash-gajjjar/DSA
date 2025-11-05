nums =  [0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1]
k = 3

max_ones = 0

for i in range(len(nums)):
    zeros_count = 0
    current_ones = 0
    for j in range(i, len(nums)):
        if nums[j] == 0:
            zeros_count += 1
        if zeros_count > k:
            break
        current_ones += 1
    max_ones = max(max_ones, current_ones)
    
print(max_ones)