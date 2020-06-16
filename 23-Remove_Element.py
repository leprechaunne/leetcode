"""
	23 - Remove Element
		Removing elements of a given value from an array with constant memory usage
		https://leetcode.com/problems/remove-element/
		Time: 	
		Space:	
        
        NOTE: This is highly optimized for very long arrays. In most small tests, this code may be slower. 
        The naive solution of switching consecutive values varies erratically based on the order of the array.
"""
class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            if nums[i] != val :
                nums[count] = nums[i]
                count +=1
        return count