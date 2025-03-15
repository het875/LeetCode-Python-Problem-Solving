
nums = [1,1,2]

class Solution:
    def removeDuplicates(self, nums ) :
           #Solution 1 with 100 % beat 
        # if len(nums) == 0 :
        #     return 0
        
        # j = 0 

        # for i in range(1 , len(nums)):
        #     if nums[i] != nums[j]:
        #         j += 1
        #         nums[j] = nums [i]

        # return j+1 
        

        #solution 2
        count = 1
        for i in range (1 , len (nums)):
            if nums[i] != nums[i-1]:
                nums[count] = nums [i]
                count += 1 
        return count