Prime number 

approach : 
    we check if the number is not less than one or one then it is not a prime number 
    then we run the loop from 2 to root n and check if there are any divisor if yes then it is not a prime number 
if not return true 








def isPrime(n):
    if n <=1 : 
        return False
    for i int range (2,(n**0.5)+1):
        if n%i== 0:
            return False 
    return True 
