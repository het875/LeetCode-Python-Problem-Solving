"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""



class Solution :
    def longestCommonPrefix(self, strs):
        if not strs :
            return ""
        
        d = {}

        for i in range(len(strs)):
            for j in range(len(strs[i])):
                if j in d:
                    d[j].append(strs[i][j])
                else:
                    d[j] = [strs[i][j]]
        print(d)
        res = ""
        for i in range(len(d)):
            if len(set(d[i])) == 1:
                res += d[i][0]
            else:
                break
        return res
    
strs = ["flower","flow","flight"]
print(Solution().longestCommonPrefix(strs))




#solution 2

class Solution:
    def longestCommonPrefix(self, strs):

        if len(strs) == 0:
            return ""
        else:
            j, k= max(strs), min(strs)
            count = 0
            print(j,k)
            for i in range(len(k)):
                if j[i] == k[i]:
                    count += 1
                else:
                    break

            print(j[:count])
            return j[:count]
        
strs = ["flower","flow","flight"]

print(Solution().longestCommonPrefix(strs))


s = ["flower","flow","flight"]
print(s[0][:2])