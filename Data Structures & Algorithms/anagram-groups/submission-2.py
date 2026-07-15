class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = defaultdict(list)

        for n in strs:
            sorted_word = "".join(sorted(n))
            anagrams[sorted_word].append(n)

        return list(anagrams.values())
                   
        