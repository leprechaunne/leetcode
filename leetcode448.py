class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            print(nums)
            x = nums[i]
            nums[i] = nums[x-1]
            nums[x-1] = x
        
        
        return [i+1 for i in range(len(nums)) if i+1 != nums[i]]


print(Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1]))

