main_str = ['abc', 'def', 'abc', 'def', 'abc', 'def', 'abc', 'def', 'abc', 'def']
sub_str = 'abc'
count = 0
for i in main_str:
    if i == sub_str:
        count += 1
print(count)
# Output: 5

main_str = "Hello this is a test string"
sub_str = "is"
count = main_str.count(sub_str)
print(count)

#using for loop
count = 0
for i in range(len(main_str)):
    if main_str[i:i+len(sub_str)] == sub_str:
        count += 1
print(count)
# Output: 2

#using while loop
count = 0
i = 0
while i < len(main_str):
    if main_str[i:i+len(sub_str)] == sub_str:
        count += 1
        i += len(sub_str)
    else:
        i += 1
print(count)
# Output: 2




# Using a For Loop with Manual Comparison (String Slicing)
main_str = "Hello this is a test string"
sub_str = "is"

count = 0
main_len = len(main_str)
sub_len = len(sub_str)

# Loop through the main_str to check for occurrences of sub_str
for i in range(main_len - sub_len + 1):  # Loop until there's enough space for the sub_str
    if main_str[i:i + sub_len] == sub_str:  # Compare the substring
        count += 1  # If it matches, increment the count

print(count)
# Output: 2

#Explaintions
"""
Explanation:
Initialization:

main_len = len(main_str): The total length of the main string.
sub_len = len(sub_str): The total length of the substring you're looking for.
For Loop:

for i in range(main_len - sub_len + 1): This loop runs through the main_str, but only goes up to a position where there's enough space left for the sub_str to fit.
String Slicing:

main_str[i:i + sub_len]: This extracts a substring of main_str starting at index i and having the length of sub_str.
Comparison:

if main_str[i:i + sub_len] == sub_str: If the sliced substring matches sub_str, it means we've found an occurrence, and we increment the count.
Result:

After the loop finishes, count will hold the total number of times sub_str was found in main_str.

"""