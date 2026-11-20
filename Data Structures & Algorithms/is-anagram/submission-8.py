# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         hashmap = {}
#         str_list = list(s)
#         check_list = list(t)
#         counter = 0

#     #turning s into a hashmap
#         for x in range(len(str_list)):
#             if str_list[x] in hashmap:
#                 hashmap[str_list[x]].append(x)
#             else:
#                 hashmap[str_list[x]] = [x]
    
#     #checking for letters in t in hashmap
#         for y in check_list:
#             if y not in hashmap:
#                 return False
#             elif hashmap[y] == []:
#                 del hashmap[y]
#                 return False
#             else:
#                 hashmap[y].pop()
#                 counter+=1
        
#         if counter == len(str_list):
#             return True
#         else:
#             return False

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS, countT = {}, {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        
        return True
    


                

            
            
