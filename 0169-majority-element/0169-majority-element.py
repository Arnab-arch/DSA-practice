class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        map={}
        for i in nums:
            if i in map:
                map[i]+=1
            else:
                map[i]=1
            if map[i] > n//2 :
                return i
            
        
        

        

        