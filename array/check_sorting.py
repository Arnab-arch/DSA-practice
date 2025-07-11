def checksort(nums):
    temp=nums[0]
    n=len(nums)
    for i in range (n):
        if temp <= nums[i]:
            temp = nums[i]
        else :
            return False 
    return True 
arr = [1,4,2,3,4,5]
print("the given array ",arr, "is sorted :" , checksort(arr))