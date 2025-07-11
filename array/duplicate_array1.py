def duplicate(nums):
    n=len(nums)
    if not nums:
        return 0 
    
    i = 0 
    for j in range (1,n):
        if nums[i]!=nums[j]:
            i+=1
            nums[i]=nums[j]
            
    return i+1
    k=i+1
nums = [1,2,3,3,3,4,4,5,6]
k=duplicate(nums)
print(f"the number of unique element is{k}" )
print(f"the modified array is :{nums[:k]}")
     

        