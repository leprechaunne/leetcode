"""
    167. Two Sum II - Input array is sorted
    https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        runner_left = 0
        runner_right = len(numbers) - 1
        
        num_left = numbers[runner_left]
        num_right = numbers[runner_right]
        
        while runner_left < runner_right:
            sum = num_left + num_right
            
            if sum == target:
                return [runner_left+1, runner_right+1]
            elif sum > target:
                runner_right -= 1
                num_right = numbers[runner_right]
            else:
                runner_left += 1
                num_left = numbers[runner_left]
        return False