class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        index = len(nums)
        counter = 0
        for x in range(index):
            for i in range(x + 1, index):
                if nums[i] == nums[x]:
                    counter += 1  

        if counter > 0:
            return True
        else:
            return False