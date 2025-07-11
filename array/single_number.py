class Solution(object):
    def singleNumber(self, nums):
        r=0
        for i in range(len(nums)):
            r=r^nums[i]
        return r 