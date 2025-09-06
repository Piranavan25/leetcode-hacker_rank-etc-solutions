class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Merge and sort the arrays
        merged = sorted(nums1 + nums2)
        m_len = len(merged)
        
        # For odd length: return middle element
        if m_len % 2 == 1:
            return float(merged[m_len // 2])  # Use integer division
        
        # For even length: return average of two middle elements
        else:
            mid1 = merged[m_len // 2 - 1]
            mid2 = merged[m_len // 2]
            return (mid1 + mid2) / 2.0