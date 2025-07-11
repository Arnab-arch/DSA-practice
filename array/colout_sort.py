nums=[2,0,2,1,1,0]
for i in range(len(nums)):
    for j in range (1,len(nums)):
        if nums[i]==nums[j]:
            nums[i+1]=nums[j]
            nums[j]=nums[i+1]
print(nums)