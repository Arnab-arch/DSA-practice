class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix = 0 
        count = 0 
        map = {0:1}
        for num in nums : 
            prefix+=num
            if prefix - k in map : 
                count+= map[prefix-k]
            map[prefix]= map.get(prefix , 0) +1 
        return count 

        
        

        




        