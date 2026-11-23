class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        res = 0
        seen = {}

        for i in range(len(s)):
            if s[i] in seen:
                l = max(seen[s[i]] + 1, l)
            
            seen[s[i]] = i
            res = max(res, i - l + 1)

        return res

# zabz
# pwwk
# abyyab
# abc
        