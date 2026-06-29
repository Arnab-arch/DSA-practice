class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # brute force would be to iterate every value and store it in sum to check and find the least but that would have time complaxity of o(n^2) ex: i = 0 intiianlly iterate j from i tp len calc total then compare totale 
        # better solution we know that each value is positive and the target is positive so if we remove one elemnt sum decreases and vice versa so its two pointer sliding window algorith 
        # we initialize l and r and the start then r will move until it finds sum or greater and if it does then we will move l and reduce one element and store everything in our asnwer to compare 

        n=len(nums)
        l=0
        sum = 0 
        min_len = float('inf')   # this is the maximun value we can store any value that we find will be less than this 
        for r in range(n):
            sum+=nums[r]
            while sum >= target :
                min_len = min(min_len , r-l+1)
                sum-=nums[l]
                l+=1
        if min_len == float('inf'):
            return 0 
        return min_len

        