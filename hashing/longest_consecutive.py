'''128. Longest Consecutive Sequence
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.


approach : 
    we just need to put thr array in a set so duplicaxtes are removed and the array is sortred then we iterate through thte number and check if the number is the first number 
    we can do that by checking if the current number - 1 == previouus number exists in the set if it does not its the first of the sequesnce , make a sub of lenght =1
    then we iterate through set until the next consequtive number exists in the set and keep increasing the sub count current+1 == next coinsecutive
     
'''







class Solution(object):
    def longestConsecutive(self, nums):
        my_set=set(nums)
        longest=0
        for i in my_set:
            if i-1 not in my_set:
                current=i
                sub=1
                while current+1 in my_set :
                    current +=1
                    sub+=1
                longest= max(longest,sub)

        return longest
        
