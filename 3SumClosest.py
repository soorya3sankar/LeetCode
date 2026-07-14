class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l=[]
        for i in range (len(nums)-2):
            for j in range (i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    m=nums[i]+nums[j]+nums[k]
                    l.append(m)
            
        closest_value = min(l, key=lambda x: abs(x - target))
        return closest_value
