class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if no number is missing the sum would be n(n+1)/2  so the actual sum minus the expected sum would give us the differene and that number is missing 
        # n=len(nums)
        # expected = n * (n+1)//2 
        # actual = sum(nums)
        # return expected - actual 

        # or we can sort this array and each index shouyld match the number at that index 
        nums.sort()
        n=len(nums)
        for i in range (n):
            if nums[i]!=i:
                return i 
        return n
