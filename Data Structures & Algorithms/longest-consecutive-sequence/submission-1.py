class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if nums == []:
            return 0
        
        nums2 = list(set(nums))
        nums2.sort()
        curr_max = 1
        curr = 1

        print(nums2)

        for i in range(1, len(nums2)):
            if nums2[i-1] == nums2[i] - 1:
                curr += 1
            else:
                curr_max = max(curr_max, curr)
                curr = 1
        
        return max(curr_max, curr)



        