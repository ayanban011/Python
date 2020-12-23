class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        a=[]
        b=0
        for i in range(len(nums)):
            if(nums[i]>0 or nums[i]<0):
                a.append(nums[i])
            else:
                b+=1
        for j in range(b):
            a.append(0)
        for k in range(len(a)):
            v=nums.pop(0)
            nums.append(a[k])
            #print(a[k],nums[k])
