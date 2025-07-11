def linearSearch( nums, target):
        n=len(nums)
        for i in range(n):
            if nums[i]== target:
                return (nums[i],i)
            
        return (None,-1)
            
target=3
nums=[2, 3, 4, 5, 3]
value,index=linearSearch(nums,target)
print("the first occurance of",value,"in nums is at index",index)
