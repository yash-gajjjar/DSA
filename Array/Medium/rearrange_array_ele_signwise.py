nums =  [2, 4, 5, -1, -3, -4]
positive, negative, full = [], [], []

for num in nums:
    if num >= 0:
        positive.append(num)
    else:
        negative.append(num)

i, j = 0, 0
while i < len(positive) and j < len(negative):
    full.append(positive[i])
    full.append(negative[j])
    i += 1
    j += 1

print("Rearranged array:", full)

