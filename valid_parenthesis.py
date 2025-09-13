class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        # Dictionary to match closing brackets to opening brackets
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:  
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                
                stack.append(char)

        
        return not stack

           
            


        