class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=0
        r=len(nums)-1
        while l < r :
            mid = (l + r )//2
            
            # we will check if the mid value is less than the next this means we can ignore the left side for now and the peak would be at the right side so we move l to mid+1 to iterate through right side 
            if nums[mid]<nums[mid+1]:
                l = mid +1
            # the mid value can be the peak element we dont want to exclude that we dont do this above for l because we already check if the adjacent value is more than the current if it is less than the current so we know the current value can be skipped 
            else :
                r = mid 
        return l

        