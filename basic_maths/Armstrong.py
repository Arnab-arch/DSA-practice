'''Check if the Number is Armstrong

You are given an integer n. You need to check whether it is an armstrong number or not. Return true if it is an armstrong number, otherwise return false.
An armstrong number is a number which is equal to the sum of the digits of the number, raised to the power of the number of digits.

Examples:
Input: n = 153
Output: true
Explanation: Number of digits : 3.
13 + 53 + 33 = 1 + 125 + 27 = 153.
Therefore, it is an Armstrong number.

link : https://takeuforward.org/plus/dsa/problems/check-if-the-number-if-armstrong

approach : 
    its simple we know how to count digits we know how to take last digit out 
    count the digitd take the number out raise them to the power and store them in a variable called sum 


time complesity : O(n)
space complexity : O(1)

'''
def isArmstrong(n):
    count = 0 
    sum=0
    original = n 
    dup = n 
    while (n>0):
        n = n //10 
        count+=1
    while (dup>0):
        d=dup%10 
        sum += d**count 
        dup = dup // 10
    if sum == original :
        return True 
    else : 
        return False
print(isArmstrong(151))


        