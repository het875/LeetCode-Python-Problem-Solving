class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # while val in nums:
        #     nums.remove(val)
        # return len(nums)
            
        # print(len(nums))

        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)  # Remove element if it's equal to val
            else:
                i += 1  # Only increment i when we don't remove an element
        return len(nums)