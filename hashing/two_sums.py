'''1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

approach : we use hashmaps for this we basically store the numbers with there index in the maps then we fidn the difference with the target given to the current number 
and if the diffrenece exists in the map those two values will add upto the target 

time complexity : O(N)
space complexity : O(N)

'''
class Solution(object):
    def twoSum(self, nums, target):
        maps={}
        for i,num in enumerate(nums):
            compliment = target - num
            if compliment in maps:
                return (maps[compliment],i)
            maps[num]=i