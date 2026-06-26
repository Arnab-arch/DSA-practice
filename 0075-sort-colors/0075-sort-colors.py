class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #brute force approach 
        #n=len(nums)
        #for i in range(n-1):
        #    for j in range(n-i-1):
        #        nums[j]>nums[j+1]
        #        nums[j],nums[j+1]=nums[j+1],nums[j]
        #return nums

        #optimal approach 
        n=len(nums)
        zero = 0 
        one = 0 
        two = 0

        for num in nums:
            if num == 0 :
                zero+=1
            elif num ==1:
                one+=1
            else:
                two+=1
        i=0
        while zero:
            nums[i]=0
            i+=1
            zero-=1
        while one:
            nums[i]=1
            i+=1
            one-=1
        while two:
            nums[i]=2
            i+=1
            two-=1
        return nums



