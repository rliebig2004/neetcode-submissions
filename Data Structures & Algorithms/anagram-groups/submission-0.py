class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = defaultdict(list) #key: list of letters, value: strings with the letters
        
        for x in strs:
            count = [0] * 26 #26 0's / elements == 26 alphabets

            for c in x:
                count[ord(c) - ord("a")] += 1 #gets the index of count at the letter <c> and adds it by 1
                
            # after count list is accounted for every letter in the string <x>, we append the string <x> to the value list
            hashmap[tuple(count)].append(x)
        
        return hashmap.values()

        

        