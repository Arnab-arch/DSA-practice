# Max Sum Subarray of size K
# Difficulty: EasyAccuracy: 49.6%Submissions: 301K+Points: 2
# Given an array of integers arr[]  and a number k. Return the maximum sum of a subarray of size k.

# Note: A subarray is a contiguous part of any given array.

# Examples:

# Input: arr[] = [100, 200, 300, 400], k = 2
# Output: 700
# Explanation: arr2 + arr3 = 700, which is maximum.
# Input: arr[] = [1, 4, 2, 10, 23, 3, 1, 0, 20], k = 4
# Output: 39
# Explanation: arr1 + arr2 + arr3 + arr4 = 39, which is maximum.
# Input: arr[] = [100, 200, 300, 400], k = 1
# Output: 400
# Explanation: arr3 = 400, which is maximum.


# optimal method is we know the size of window is fixed because k in const so we just need to first 
# find sum of first k elements in the array then we just move the window so 
# we use for loop to move through the array for each element added the window will move 
# and the first element will be removed 
# example :

# [1,2,3,4,5,6,7]   k= 2 
# so first we need sum of k element first k elements so we just use sum function sum(arr[:k])
# sum = 3 
# now this we assume is the max of the valuess 
# then we move i from k to n because we have already calculated till k 
# so now i = k for first iteration  = 3 arr[k] = 3 then we add 3 in our window sum and minus the 
# first value because we are starting from start we need to add 3 and subtract 1 to maintain the 
# lenght of the subarray to be k 
# so we do i-k so now i=k+1=3 arr[i]= 4 and we need to remove 2 so 2 is arr[3-2]=arr[1]
# now i = k+2=4 arr[4]=5 we need to remove 3 so 3 is arr[4-2]=arr[2]=3



class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
        window = sum(arr[:k])
        maxsum = window 
        n=len(arr)
        for i in range(k,n):
            window+=arr[i]-arr[i-k]
            maxsum = max(window , maxsum)
        return maxsum


sol = Solution()

print(sol.maxSubarraySum([100,200,300,400],2))
print(sol.maxSubarraySum([1,4,2,10,23,3,1,0,20],4))
print(sol.maxSubarraySum([100,200,300,400],1))


        # time complexity loops runs once thus o(n) and space is 0(1)