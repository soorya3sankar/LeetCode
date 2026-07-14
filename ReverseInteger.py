class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1
        x = abs(x)
    
        rev = 0
        while x != 0:
            pop = x % 10      
            x //= 10          
            rev = rev * 10 + pop
        
   
        m=rev * sign
        
        if m < pow(-2,31) or m > pow(2,31)-1:
            return 0
            
        return m
        
