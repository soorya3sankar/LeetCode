class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_set = set()
        max_length = 0
        left = 0
        
        for right in range(len(s)):
            # Shrink window from the left until the duplicate is removed
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
                
            # Add the new character and update max length
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
            
        return max_length
        
