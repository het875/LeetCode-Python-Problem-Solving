class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        # solution 1 with 0 ms , 100 beat 
        # left, right = 0, len(nums) - 1
        
        # while left <= right:
        #     mid = (left + right) // 2  # Find the middle index
            
        #     if nums[mid] == target:
        #         return mid  # Target found, return its index
        #     elif nums[mid] < target:
        #         left = mid + 1  # Narrow the search to the right half
        #     else:
        #         right = mid - 1  # Narrow the search to the left half
        
        # # If the target is not found, `left` will be the index where it should be inserted
        # return left


# =========================================================================================================================

        # Solution 2 with 100 % beat 

        for i in range(len(nums)):
            if nums[i] == target:
                return i  # If the target is found, return the index
            elif nums[i] > target:
                return i  # If the current element is greater than target, return the current index
        # If the target is larger than all elements, return the next position (end of the list)
        return len(nums)