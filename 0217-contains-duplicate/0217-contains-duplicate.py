class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # new_array = []
        # for i in nums:
        #     if i in new_array:
        #         return True
            
        #     new_array.append(i)
        # return False 

        seen = set(nums)
        if len(seen)!= len(nums):
            return True
        return False



