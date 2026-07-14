class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # given int nums an array and integer target o(log(n)) should be the time complexity 
        # first of all generic looping or iteration wont work 
        # two pointer and sliding window wont work as there is negative here 
        # we have to return the index of the number 
        # see the array is sorted so we can look at the mid value of the array if target is greater than mid value we search the right side if target is less that mid value we search the lest side so we can reduce time cpmplexity like that 
        left = 0 
        right = len(nums)-1
        while left<=right:
            mid = left + (right - left ) // 2     # mid value 
            if nums[mid] == target:     
                return mid 
            elif nums[mid] < target:     # if mid is less than T we need only the right side 
                left = mid+1
            else :
                right = mid - 1
        return -1

        