'''Divisors of a Number

You are given an integer n. You need to find all the divisors of n. Return all the divisors of n as an array or list in a sorted order.
A number which completely divides another number is called it's divisor.

Examples:
Input: n = 6
Output = [1, 2, 3, 6]
Explanation: The divisors of 6 are 1, 2, 3, 6.

time and space : O(n) and O(n)






def divisor(n):
    arr=[]
    for i in range (1,n+1):
        if n % i == 0 :
            arr.append(i)
    return arr 
print(divisor(6))

optimal approach : 
 we take the range from 1 to n**0.5 root n because a number is paired till half of the range so we dont have to check till n 
 every number there exits all the function exists in pair of number if from 1 to root of the that number . 
 so if we are going to check for all the numbers that are divisible by N 
 so now the question arises what about the other number that is paired with the number we just found let us supose that is i 
 its simple the other number would be N // i --------------- very important 
 
 so if we get a number i that devides the N completely ---------- first number is i 
 then N // i = val ----------------------------------- this val would be the second number 
 '''
def divisor(n):
    arr=[]
    for i in range (1,int(n**0.5)+1):
        if n % i == 0 :
            arr.append(i)
            arr.append(n//i)
    return arr 
print(divisor(6))
 time complexity now is O(logn)
 