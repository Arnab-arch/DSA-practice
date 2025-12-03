'''
lC 509
link : https://leetcode.com/problems/fibonacci-number/description/

approach : 
    fibonacci goes by 0,1,1,2,3,5,8,13........................
    initial value will always be 0, 1
    after that next digit  is just the sum of the first two digits 

     
space complexity : O(1)
time complexity :O(n)
'''
def fibonacci(n):
    a=0
    b=1
    for i in range (2,n+1):
        c=a+b
        a=b
        b=c 
    return c 
print(fibonacci(3))