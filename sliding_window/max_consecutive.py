'''1004. Max Consecutive Ones III
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

link:https://leetcode.com/problems/max-consecutive-ones-iii/description/

approach : 
    we just take the subarray and find the largest subarray with consecutive 1's and we take the valid subarray with k number of zeroes 
    we make a subaray with maximum consecutives 1,s including K no of zeroes 


'''

class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l=0           #initial L
        z=0           #zero counter 
        max_sub=0     #store max_sub
        n=len(nums)
        for r in range (n):         #expand window 
            if nums[r]==0:
                z +=1                   # increase the count of zeros
            while (z>k):           # array becomes invalid time to move the subarray or the window to match cond    
                if nums[l] == 0 :        # if left hand side is zero then reduce the count of zero 
                    z-=1           #make space for extra zero as we are moving L 
                l+=1               #keep moving L until you you have the required number of K zeroes 
            w=r-l+1                # note current subarray 
            max_sub=max(max_sub,w)        #store and compare with max and update it 
        return max_sub                        
