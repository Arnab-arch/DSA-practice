nums=[3,3,5,7]
n=len(nums)
max= nums[0]
for i in range (n):
    if max < nums[i]:
        max=nums[i]
        
print(max)
temp=float('-inf')
for i in range (n):
    if nums[i]!=max and nums[i]>temp:
        temp=nums[i]
print(temp)