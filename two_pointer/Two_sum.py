167. Two Sum II - Input Array Is Sorted

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers index1 and index2, each incremented by one, as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].


# brute force here is basically we run two loops check to check each value or we can use a 
#hashmap put each values and check with the previous value but for there one is O(n^2) and other will take o(n)


# optimal approach here is we take two indices one at the beginning other at the end we call it L and R 
# now we check the value on these 2 indices is it equal to our target 
# the important part here would be the array is sorted so we know at the begiining the value is least 
# and at the end the value is the largest so
# example :- suppose we have two numbers 2 and 8 and and our target is 5 
# so if we add 2+8=10>5 so logically we will move 8 because its the bigger value moving 2 will not do anythig 
# and if the sum is less than target we have to move 2 because we need to increment the value and we move lef side if we have to decrement the value 
# we use while loop here because we have a condition l<r and we want to check everynumber 
#while loop helps us iterate with our condition instead of not following that 


## optimal approach 

def 2sum(numbers,target):
    n= len(numbers)
    l=0
    r=n-1
    while l<r:
        sum = numbers[l]+numbers[r]
        if sum === target :
            return (l+1,r+1)
        elif sum < target:
            l+=1
        else:
            r+=1
    



    
