class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        count=0
        l=0
        max_len=0
        for r in range(n):
            if nums[r] == 0:
                count+=1
            while count>1:
                if nums[l] == 0:
                    count-=1
                l+=1
            max_len = max(max_len, r-l)
        return max_len

            