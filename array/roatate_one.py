def rotate(nums,k):
    n=len(nums)
    first=nums[0]
    for j in range(k):
        for i in range(1,n-1):
            nums[i+1]=nums[i]
    first = nums[n-1]
    nums[n-1]=first 
    return nums
nums=[1,2,3,4,5,6,7]
print("the rotated array by one to the left is :",rotate(nums,3))