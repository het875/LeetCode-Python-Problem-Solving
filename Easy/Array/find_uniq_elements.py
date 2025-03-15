a = [1, 2, 3, 4, 9, 5, 6, 1, 2, 5]

unique = []
repeated = []

# To keep track of occurrences
seen = []

for item in a:
    if item not in seen:
        seen.append(item)
        unique.append(item)
    else:
        if item not in repeated:
            repeated.append(item)

print("Unique Array:", unique)
print("Repeated Array:", repeated)

"""
Unique Array: [1, 2, 3, 4, 9, 5, 6]
Repeated Array: [1, 2, 5]
"""


a = [1, 2, 3, 4, 9, 5, 6, 1, 2, 5]

unique = []
repeated = []

# Iterate over each element of the array
for i in range(len(a)):
    # Check if the element is already in unique or repeated
    if a[i] not in unique and a[i] not in repeated:
        unique.append(a[i])
    elif a[i] not in repeated:
        repeated.append(a[i])

print("Unique Array:", unique)
print("Repeated Array:", repeated)


#  Using a Dictionary to Track Occurrences (Manually Implementing Counting)
a = [1, 2, 3, 4, 9, 5, 6, 1, 2, 5]

unique = []
repeated = []
count_dict = {}

# Create a manual count dictionary
for num in a:
    if num not in count_dict:
        count_dict[num] = 1
    else:
        count_dict[num] += 1

# Now, classify numbers into unique or repeated
for num in count_dict:
    if count_dict[num] == 1:
        unique.append(num)
    else:
        repeated.append(num)

print("Unique Array:", unique)
print("Repeated Array:", repeated)



# Using a List to Track Duplicates
a = [1, 2, 3, 4, 9, 5, 6, 1, 2, 5]

unique = []
repeated = []
seen = []

for num in a:
    if num not in seen:
        seen.append(num)
        unique.append(num)
    elif num not in repeated:
        repeated.append(num)

print("Unique Array:", unique)
print("Repeated Array:", repeated)


# Using a "Seen" List to Track First Occurrences
a = [1, 2, 3, 4, 9, 5, 6, 1, 2, 5]

unique = []
repeated = []
seen = []

for num in a:
    if num not in seen:
        seen.append(num)
        unique.append(num)
    elif num not in repeated:
        repeated.append(num)

print("Unique Array:", unique)
print("Repeated Array:", repeated)
