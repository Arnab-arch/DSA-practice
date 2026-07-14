class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        # solution 1 can be find the ASCI quivalent of the target then find the mid value of the array then we can check if the mid value is greater than or less than target if less that target we just need to check on right side if grater than target we need to check the right side 
        # the case would be different if the array wasnt sorted because then we would have to ask the interviewer can we assume capital alphabets or numbers or everything is small and then we cant solve using binary search as the unsorted array may have the asnwer on the either side doesnt matter about the mid point 
        # and we dont need python ord in this because pyhton compares the values in lexicographically order automatically 
        ch = ord(target)
        left =0 
        right = len(letters) - 1
        ans = letters[0]
        while left<=right:
            mid = left + (right-left)//2
            if letters[mid] > target :
                ans = letters[mid]
                right = mid - 1
            else :
                left = mid + 1

        return ans 


        