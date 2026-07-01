class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # brute force 
        # l=0 
        # n=len(nums)
        # counter = 0 
        # product =1
        # if k%nums[0]==0:
        #     counter+=1
        # for r in range(1,n):
        #     if k%nums[r]!==0:
        #         counter+=1
        #         product=product*nums[r]
        #     if  product < k :
        #         counter+=1
        #     else :
        #         product = product / nums[l]
        #         l+=1
        # return counter

        l=0 
        counter =0
        product = 1
        for r in range(len(nums)):
            product*=nums[r]

            while product >=k:
                product//=nums[l]
                l+=1
            
            counter += r-l+1
        return counter 


        # single loop so O(n) time complexity 
