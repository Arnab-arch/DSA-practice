'''
. Reverse Integer
Medium
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
Example 1:
Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1

link : https://leetcode.com/problems/reverse-integer/

approach : we know that to reverse a number we first need the last digit and put it in the first one 
now we should focus on ones and tens 
ex: 341 the 3 is in 100's and 1 is in 1,s now 1 have to be 100 + 40 + 3 
to do that first how do we get the number 14 == 10 + 4 
we know d (last digit) == 1 after first module then d(second last) = 4 
now can we write 1*10 + 4 
yes we can 
and then 14 * 10 + d (3) = 140 + 3 == 143 which is our answer 
thus rev = 0 (initially )
rev = (rev *10 ) + d 
 Time and Space Complexity
 Time Complexity: O(log₁₀x) or simply O(d)
Where d is the number of digits in the input number x.

Because we process one digit at a time (via %10 and //10), the number of iterations = number of digits.

 Space Complexity: O(1)
Only a few variables (rev, x, sign, d) are used.

No extra space or data structures are needed.

code :: 
'''
class Solution(object):
    def reverse(self, x):
        if x<0:
            sign = -1
        else :
            sign = 1
        rev = 0 
        x=abs(x)
        while (x>0):
            d=x%10 
            x=x//10
            rev = (rev*10)+d
        if -2**31 <= rev >= 2**31 - 1:
            return 0 

        return sign*rev
