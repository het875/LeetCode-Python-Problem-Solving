class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        # r = ""

        # for i in range(len(words)):
        #     r += words[i]

        #     if len(r) >= len(s):
        #         break
        
        # if len(r) != len(s):  
        #     return False
        
        # for i in range(len(s)):
        #     if r[i] != s[i]:
        #         return False


        prefix = ""
        
        for word in words:
            prefix += word  
            
            if prefix == s:
                return True
            
            if len(prefix) > len(s):
                break
        
        return False