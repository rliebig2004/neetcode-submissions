class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)
        for s in strs:          #O(m) - going through each list
            count = [0] * 26    #note the freq instead of sort
            for c in s:         #O(n) - going through each char
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)

        return list(res.values())


        