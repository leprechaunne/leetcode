"""
	23 - Remove Element
		Removing elements of a given value from an array with constant memory usage
		https://leetcode.com/problems/remove-element/
		Time: 	
		Space:	
        
        NOTE: This is highly optimized for very long arrays. In most small tests, this code may be slower. 
        The naive solution of switching consecutive values varies erratically based on the order of the array.
"""

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        #EDGE CASE: No array
        if(len(nums) == 0):
            return 0
        #EDGE CASES: One value in array
        elif(len(nums) == 1):
            if(nums[0] == val):
                return 0
            else:
                return 1
        
        
        
        # Use one runner to iterate and one to mark the end of the "new" list
        end = len(nums) - 1 #marks the end of the array, which can also calulate len
		# Find and swap
        i = 0
        while(i < end):
			# Adjust end to position with a "good" value
            while((end >= 0) and (nums[end] == val)): #edge case requires value of end be checked to avoid exception
                end -= 1

			# Now check position at the runner for value
			# if a swap must happen, make sure the target val is pushed to the back
            if(nums[i] == val):
                nums[i] = nums[end]
                nums[end] = val
			
            #increment 1
            i += 1
        
        
        #EDGE CASE: Array filled with target value
        #   ==> set end to -1 so length at return is 0
        if(nums[0] == val and nums[1] == val):
            end = 0
        #EDGE CASE: Array filled with target value except for one
        #   ==> set end to 0 so length at return is 1
        elif(nums[0] == val or nums[1] == val):
            end = 1
            #EDGE CASE: Such an array needs a final swap
            if(nums[1] != val):
                nums[0] = nums[1]
                nums[1] = val
        
        #return length (adjusted for 0 index)
        return end
