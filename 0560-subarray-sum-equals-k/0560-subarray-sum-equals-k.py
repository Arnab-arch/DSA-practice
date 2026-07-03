class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # this answer is wrong because sliding window doesnt work for negative numbers in an array it breaks 
        # l= 0 
        # n=len(nums)
        # sum=0
        # counter=0 
        # for r in range(n):
        #     sum+=nums[r]
        #     if sum==k:
        #         counter+=r-l+1
            
        #     while sum > k :
        #         sum-=nums[l]
        #         l+=1

            
        # return counter
        sum =0
        prefixmap={0:1}
        count=0
        for num in nums:
            sum+=num

            if sum-k in prefixmap:
                count+=prefixmap[sum-k]
            prefixmap[sum]=prefixmap.get(sum,0)+1
        return count

    

