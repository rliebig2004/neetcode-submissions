# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
        
#         for i in range(len(nums)):
#             for n in range(i+1, len(nums)):
#                 if (nums[i] + nums[n]) == target:
#                     return [i, n]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        prevMap = {} #number, index

        for i, n in enumerate(nums): #index, value
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        

        