nums = [1, 2, 2, 4, 3, 1, 4, 3, 8]
unique_number = 0

for num in nums:
    unique_number ^= num  # XOR operation
    
print(unique_number)