# Problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l= 0
        result = 0
        charSet= set()
        
        for r in range (0,len(s)):
            
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            result= max(result, (r-l)+1)
        return result
