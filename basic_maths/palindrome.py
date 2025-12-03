'''Palindrome Number
Solved
Easy
Topics
premium lock icon
Companies
Hint
Given an integer x, return true if x is a palindrome, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 

link : https://leetcode.com/problems/palindrome-number/

approach : we know how to find the reverse of a number 
take absolute remove last digit put it in the formula == rev*10 + d and keep going until the number ends 
now make one suplicate of the original number for finding rev our original number becomes 0 thus a duplicate to compare 
time complexity : 0(xlogn)
space complexity : o(1)

def isPalindrome( x):
    
  
    if x < 0 :
        return False 
    rev = 0 
    dup = x                                        # we make a duplicate copy because after we are done with the loop x becomes 0 so we cant compare that 
                                                   # thus we make a dup and compare it with the original                                                   
    while (x>0):
        d= x % 10 
        x = x // 10 
        rev = (rev*10) + d 
                                
    if rev == dup  :
        return True 
            
print(isPalindrome(121))
'''