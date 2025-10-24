nums = [2, 3, 4, 5, 3]
target = 8
found_index = -1 

for i in range(len(nums)):
    if nums[i] == target:
        found_index = i
        break

print(found_index) 