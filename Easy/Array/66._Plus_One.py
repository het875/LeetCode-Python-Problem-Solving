class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        # Start from the last digit and move backwards
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1  # No carryover, just add 1 and return the result
                return digits
            digits[i] = 0  # If the digit was 9, set it to 0 and carry over
        
        # If we reached here, it means all digits were 9, so we need to add a 1 at the beginning
        return [1] + digits  # Add 1 at the beginning (e.g., [9, 9] becomes [1, 0, 0])

