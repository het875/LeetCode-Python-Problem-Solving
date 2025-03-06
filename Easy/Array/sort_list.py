data_list = [-5, -23, 5, 0, 23, -6, 23, 67]
new_list = []

while data_list:
    minimum = data_list[0]  # arbitrary number in list 
    for x in data_list: 
        if x < minimum:
            minimum = x
    new_list.append(minimum)
    data_list.remove(minimum)    

print (new_list)




l = [64, 25, 12, 22, 11, 1,2,44,3,122, 23, 34]

for i in range(len(l)):
    for j in range(i + 1, len(l)):

        if l[i] > l[j]:
           l[i], l[j] = l[j], l[i]

print (l)




nums = [5,2,23,45,1,22,6,4,8,9,26,30,32,54,70]


def bubble_sort(nums):
    for i in range(0 , len(nums)):
        for j in range (i+1 , len(nums)):
            if nums[i] >= nums[j] :
                nums[i] , nums[j] = nums[j] , nums[i]
    return nums
nums = [5,2,23,45,1,22,6,4,8,9,26,30,32,54,70]
print( bubble_sort(nums))      


# Descenting order sort
def bubble_sort_desc(nums):
    for i in range(0 , len(nums)):
        for j in range (i+1 , len(nums)):
            if nums[i] <= nums[j] :
                nums[i], nums[j] = nums[j], nums[i]
    return nums

print(bubble_sort_desc(nums))

