nums = [1, 2, 1, 1, 3, 2, 2]

maj_ele = len(nums) // 3

frequency = {}
new = []

for num in nums:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
        
print(frequency)
        
for key, value in frequency.items():
    if value > maj_ele:
        new.append(key)

print(new)