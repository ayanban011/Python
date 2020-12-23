from sys import maxint
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        max_so_far = -maxint - 1
        max_ending_here = 0
        for i in range(0, size): 
            max_ending_here = max_ending_here + nums[i] 
            if (max_so_far < max_ending_here): 
                max_so_far = max_ending_here 
  
            if max_ending_here < 0: 
                max_ending_here = 0   
        return max_so_far 
        
