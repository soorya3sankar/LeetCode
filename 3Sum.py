class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        f=set()
        f=list()
        for i in range (len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
            
                    if(nums[i]+nums[j]+nums[k]==0):
                        
                        l=sorted([nums[i],nums[j],nums[k]])
                        if l not in f:
                            f.append(l)
        return f
        
