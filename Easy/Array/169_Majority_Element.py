"""

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:
Input: nums = [3,2,3]
    Output: 3

    
Example 2:
Input: nums = [2,2,1,1,1,2,2]
    Output: 2

"""



class Solution:
    def majorityElement(self, nums):
        # dic = {}
        
        # for i in nums:
        #     if i in dic :
        #         dic[i]+= 1
        #     else:
        #         dic[i] = 1
        
        
        # print(dic)

        # m_ele = max(dic , key = dic.get)
        # print(m_ele)
        # return m_ele


        #solutions 2:

        # val = 0
        # maj = None
        # for num in nums:
        #     if val == 0:
        #         maj = num
        #     if num == maj:
        #         val += 1
        #     else:
        #         val -= 1
        # return maj





        #Solutins 3

        nums.sort()
        num_amount = len(nums)
        return nums[num_amount//2]