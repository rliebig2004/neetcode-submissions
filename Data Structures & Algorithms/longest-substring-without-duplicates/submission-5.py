class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        longest = 0
        mp = {}
        
        for r in range(len(s)) :
            if s[r] in mp:
                l = max(l, mp[s[r]] + 1)
            mp[s[r]] = r
            longest = max(longest, r - l + 1)

        return longest

# zabz
# pawwk
# abyyab
        