'''Reverse an array
Given an array arr of n elements. The task is to reverse the given array. The reversal of array should be inplace.

Examples:
Input: n=5, arr = [1,2,3,4,5]
Output: [5,4,3,2,1]
Explanation: The reverse of the array [1,2,3,4,5] is [5,4,3,2,1]

Input: n=6, arr = [1,2,1,1,5,1]
Output: [1,5,1,1,2,1]
Explanation: The reverse of the array [1,2,1,1,5,1] is [1,5,1,1,2,1].

approach 1 : 
    we will use new array 
    now we create a new array in the name of new of the same length as the original array . now we run a loop from the end of the loop to the start with -1 step 
    now just equate the fisr element of the new array to the original array last element 
    new[n-i-1]=arr[i]
    
def reverse(arr,n): 
    new = [0]*n
    for i in range (n-1,-1,-1):
        new[n-i-1]=arr[i]
    return new 
print(reverse([1,2,3,4,5],5))
'''
#approach 2 : (two poinet method)

my logic fault : i thought that i have to assign two pointers beginning and the end and run a for loop and equate the elemets the pointer points at 
it is wrong because after the mid element the numbers would repeat itself and its wrong 

correct approach : 
    run a while loop one pointer at the start one at the end now the condition for the loop is it will change value of last digit before the mid value 
    and we increment and decrement the pointers value as we go  
        
                
def reverse(arr,n):
    p1=0
    p2=n-1
    while p1<p2:
        arr[p1],arr[p2]=arr[p2],arr[p1]
        p1+=1
        p2-=1
    return arr 
print(reverse([1,2,3,4,5],5))