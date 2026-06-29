
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
 # this is a brute force solution simple but it has the time complexity of o(logn)
       # squares=[]
       # for num in nums:
       #     squares.append(num*num)
       # squares.sort()

       # return squares
# we know that if wecompare two values at the start and at the end and whichever absolutte value is greater that the other would be places at the end because the array is sorted already 
        n=len(nums)
        ans=[0]*n    # we do these because we need placeholder otherwise error will be index out of range 
        l=0
        r=n-1
        position = n-1
        while l<=r:
            if abs(nums[l])>abs(nums[r]):
                ans[position]=nums[l]*nums[l]
                l+=1
            else:
                ans[position]= nums[r]*nums[r]
                r-=1
            position-=1
        return ans
        

        





        