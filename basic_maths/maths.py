'''1)Count all Digits of a Number
Easy
You are given an integer n. You need to return the number of digits in the number.
The number will have no leading zeroes, except when the number is 0 itself.
Examples:
Input: n = 4
Output: 1
Explanation: There is only 1 digit in 4.

link : https://takeuforward.org/plus/dsa/problems/count-all-digits-of-a-number

approach :
    whenever a number is given we should know 
    we cant run a for loop in this as num are not iterable 
    we cant use functions such as len/split etc .
    
    trick :
        try deviding multyplying and playinf with number as a whole 
        here :
            if you want the last digit of a number you would need reminder 
            if you want to remove the last digit of the number you would need //
    case 1:
        what we do is we take our number check if it is greater than 0 
        then we put it in while loop and with every iteration :
            we get the last digit by n%10 then increase the count 
            then update the number by n // 10  --- remove the last digit 

def digits(n):
    count=0
    while n> 0:
        d=n%10
        count+=1
        n=n//10
    return count 
print(digits(3456))
=========================================================================================================================================================
7. Reverse Integer
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
'''

            