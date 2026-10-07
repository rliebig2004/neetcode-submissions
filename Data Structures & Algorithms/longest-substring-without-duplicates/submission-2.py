class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = {}
        res = 0

        for i in range(len(s)):
            if s[i] in seen:
                l = max(seen[s[i]] + 1, l) #comparing with itself for double duplicates so left pointer doesn't go backwards

            seen[s[i]] = i # keeps track of current substring and updates to latest index of duplicated letter

            res = max(res, i - l + 1)

        return res
        