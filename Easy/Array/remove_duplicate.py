nums = [1,2,5,3,6,4,8,1,2,6,3,6,7,9,2,6,9,1]
nums.sort()
print(nums)
uniq = []

for i in range(len(nums)):
    if nums[i] not in uniq:
        uniq.append(nums[i])

print(uniq)


nums = [1, 2, 5, 3, 6, 4, 8, 1, 2, 6, 3, 6, 9, 2, 6, 9, 1]
nums.sort()  # Sort the list first
print("Sorted nums:", nums)

uniq = []  # List to store unique numbers

i = 0
while i < len(nums):
    # Check if the current element is a duplicate (by looking ahead in the list)
    if nums[i] in nums[i+1:]:
        nums.pop(i)
    else:
        uniq.append(nums[i])
        i += 1  # Move to the next element only if it's unique

# Print the final list of unique numbers
print("Unique nums:", uniq)


