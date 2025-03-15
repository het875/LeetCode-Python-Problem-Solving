"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4."""

""" """




class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Define the mapping of Roman numerals to integer values
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        pre_vl = 0  # Holds the value of the previous Roman numeral
        total = 0  # Accumulator to store the final result

        # Traverse the string in reverse order (right-to-left)
        for char in reversed(s):
            cr_val = roman[char]  # Get the integer value of the current Roman numeral
            
            # If the current value is greater than or equal to the previous value
            if cr_val >= pre_vl:
                total += cr_val  # Add it to the total
            else:
                total -= cr_val  # Otherwise, subtract it (because it's part of a subtractive combination)

            # Update the previous value for the next iteration
            pre_vl = cr_val

        return total



# Explanation:
"""The Logic Behind the Code:
Roman Numerals Subtraction Rule:
Normally, Roman numerals are written in descending order (from largest to smallest). For example, VIII means 5 + 1 + 1 = 7.
However, when a smaller numeral comes before a larger numeral, it's subtracted. For example, IV means 5 - 1 = 4, because "I" is before "V".
Reverse Processing:
The key trick here is processing the Roman numeral string from right to left (i.e., from the last character to the first one).
This is because the subtraction rule (e.g., IV = 4) only happens when a smaller numeral comes before a larger one. So, when we go from right to left, we can easily compare the current numeral to the next numeral (which we already processed).
Greedy Addition and Subtraction:
As we move from right to left:
If the current numeral is larger than or equal to the numeral we just processed (the one on the right), we add it to our total.
If the current numeral is smaller than the numeral we just processed (the one on the right), we subtract it from the total.
Simple Example Walkthrough:
Let’s take the Roman numeral "MCMXCIV" (which means 1994) and break it down step by step:

Initial Setup:

We start with a total of 0 and the previous value (pre_vl) is also 0.
Start from the Rightmost Character:

Last character: "V" → value is 5. Add 5 to the total: total = 5.
Update the previous value (pre_vl = 5).
Next Character:

"I" → value is 1. Since 1 is less than 5 (the previous value), we subtract 1 from the total: total = 5 - 1 = 4.
Update previous value (pre_vl = 1).
Next Character:

"C" → value is 100. Since 100 is greater than 1, we add 100 to the total: total = 4 + 100 = 104.
Update previous value (pre_vl = 100).
Next Character:

"X" → value is 10. Since 10 is less than 100, we subtract 10 from the total: total = 104 - 10 = 94.
Update previous value (pre_vl = 10).
Next Character:

"M" → value is 1000. Since 1000 is greater than 10, we add 1000 to the total: total = 94 + 1000 = 1094.
Update previous value (pre_vl = 1000).
Next Character:

"C" → value is 100. Since 100 is less than 1000, we subtract 100 from the total: total = 1094 - 100 = 994.
Update previous value (pre_vl = 100).
First Character:

"M" → value is 1000. Since 1000 is greater than 100, we add 1000 to the total: total = 994 + 1000 = 1994.
Update previous value (pre_vl = 1000)."""