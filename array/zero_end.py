
def zeromoves(nums):
    n=len(nums)
    count=0
    pos=0
    for j in range (n):
        if nums[j]==0:
            count+=1
        else:
            nums[pos]=nums[j]
            pos+=1 
    for j in range (pos,n):
        nums[j]=0
    return nums 
nums=[0,1,0,3,12]
print("output",zeromoves(nums))
            
            
    