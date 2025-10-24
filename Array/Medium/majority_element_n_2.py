nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]

maj_ele = len(nums) // 2

frequency = {}

for num in nums:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
        
# print(frequency)

for key, value in frequency.items():
    if value > maj_ele:
        print(key)