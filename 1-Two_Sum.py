"""
    1. Two Sum
    https://leetcode.com/problems/two-sum/
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # compliment_map - dict storing possible solution numbers with pointers to the given index
        compliment_map = {}
        
        for i, x in enumerate(nums):
            compliment = target - x
            # print("i=",i,"   map=",compliment_map) 
            
            if compliment in compliment_map:
                return [compliment_map[compliment], i]
            else:
                compliment_map[x] = i
        
        return False
            
        