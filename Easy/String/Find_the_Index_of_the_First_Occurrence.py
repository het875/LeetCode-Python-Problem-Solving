"""

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1
        

haystack = "sadbutsad"
needle = "sad"

print(Solution().strStr(haystack, needle))


haystack = "leetcode"
needle = "leeto"
print(Solution().strStr(haystack, needle))


#Output: 0

#Output: -1


# Solution 2

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        1. first we trawels str.
        2. then we check the needle == haystack
        3. check if len of needle is less then haystack
        """
        if needle in haystack:
            return haystack.index(needle)
        return -1
    
haystack = "sadbutsad"
needle = "sad"


print(Solution().strStr(haystack, needle))



