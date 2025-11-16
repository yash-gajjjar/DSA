s = "ccabcc"
target_chars = {'a', 'b', 'c'}
count = 0

for i in range(len(s)):
    for j in range(i, len(s)):
        substring = s[i : j + 1]
        valid = all(char in substring for char in target_chars)
        
        if valid:
            #print(substring)
            count += 1
print(count)        