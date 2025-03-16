"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

"""

class Solution:
    def isValid(self, s: str) -> bool:

        #Solution : 1
        # stack = []

        # for i in s :
        #     if i == '(' :
        #         stack.append(')')
        #     elif i == '[' :
        #         stack.append(']')
        #     elif i == '{' :
        #         stack.append('}') 
        #     elif not stack or stack.pop() != i:
        #         return False

        # return stack == []



        #solution : 2
        # Initialize dictionaries to count opening and closing brackets
        open_count = {'(': 0, '{': 0, '[': 0}
        close_count = {')': 0, '}': 0, ']': 0}
        
        # Iterate through each character in the string
        for char in s:
            # If it's an opening bracket, increment the corresponding open counter
            if char in open_count:
                open_count[char] += 1
            # If it's a closing bracket, increment the corresponding close counter
            elif char in close_count:
                close_count[char] += 1
                # Check if the closing bracket exceeds the opening bracket count
                if close_count[char] > open_count[char]:
                    return False
        
        # Ensure that opening and closing brackets are balanced for each type
        return open_count == close_count





        #Solution : 3
        # Counters for opening and closing brackets
        # open_paren, open_curly, open_square = 0, 0, 0
        # close_paren, close_curly, close_square = 0, 0, 0
        
        # for char in s:
        #     if char == '(':
        #         open_paren += 1
        #     elif char == ')':
        #         close_paren += 1
        #     elif char == '{':
        #         open_curly += 1
        #     elif char == '}':
        #         close_curly += 1
        #     elif char == '[':
        #         open_square += 1
        #     elif char == ']':
        #         close_square += 1
            
        #     # Check at any point, if closing brackets outnumber opening ones
        #     if close_paren > open_paren or close_curly > open_curly or close_square > open_square:
        #         return False
        
        # # Check that opening and closing counts match for each bracket type
        # return open_paren == close_paren and open_curly == close_curly and open_square == close_square









#Example 1
s = "()"
print(Solution().isValid(s)) #Output : True

#Example 2
s = "()[]{}"
print(Solution().isValid(s)) #Output : True

#Example 3
s = "(]"
print(Solution().isValid(s)) #Output : False
