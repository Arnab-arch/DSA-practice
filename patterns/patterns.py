'''1) *****   
   *****
   *****
   *****
   *****
approach :
    we devide every pattern in two parts one is rows and the other is columns 
    now imagine a n*m matrix and we see the places or observe the pattern of rows with respect to columns 
    now rows are horizontal  lines and columns are vertical lines 
    every pattern is just a relation between rows and columns and the space of the matrix we just have to identify that 
    
    tip1: 
        observe i iterate it till you can see it in the patters and then j runs inside i so observe for every iteration of i how does j change 
        find common pattern in that in form of N , i or j :
    in this we can see for every iteratoin of i j travels from (0,n)
    thus if i =0 then j varies from 0,1,2,3,4
    
    time complexity = o(n^2)
    space complexity = o (1) output usess no extra data structures and print is done sirectly not stored 

# code 
def pattern(n):
    for i in range (n):
        for j in range (n):
            print ("*" ,end = "")
        print()  #  moves to the next line 
pattern(5)

2) *
   **
   ***
   ****
   *****
approach :
    now when i = 0 (fisrt row )
    j = 0 (first colums )
    when i = 3 , j = 3 
    so we see i = j ; 
     
    time complexity = o(n^2)
    space complexity = o (1) output usess no extra data structures and print is done sirectly not stored 
code :


def pattern(n):
    for i in range (n+1):
        for j in range (i):
            print ("*" ,end = "")
        print()  #  moves to the next line 
pattern(5)

3)    a pyramid 
   
def pattern(n):
    for i in range (0,n-1//2+1):
        for j in range ((n-1/2)-i , (n-1/2)+i+1):
            print ("*" ,end = "")
        print()  #  moves to the next line 
pattern(9)   
'''