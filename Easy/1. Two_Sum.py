nums =  [2,7,11,15]

target = 9

class Solution:
    def twoSum(self, nums, target: int):
        for i in range(0 , len(nums)-1):
            for j in range (i+1 , len(nums)):
                if (nums[i] + nums[j] == target) :
                    return [i,j] 
                
