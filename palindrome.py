class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        #str(x)[::-1] this will reverse the string

        return str(x) == str(x)[::-1]