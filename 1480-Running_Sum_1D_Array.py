""" 
    1480 - Running Sum of 1d Array - 
    https://leetcode.com/problems/running-sum-of-1d-array/
        Time    =   O(n) [O(2n)]
        Space   =   O(1)
"""

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # iteratively add sum to previously finished value
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
            
        return nums
        