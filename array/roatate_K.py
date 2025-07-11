'''def rotate_element(nums, k):
    n = len(nums)
    k = k % n
    
    arr1 = []  
    arr2 = []  

    
    for i in range(n - k, n):
        arr1.append(nums[i])
    

    for i in range(0, n - k):
        arr2.append(nums[i])
    
    new_array = arr1 + arr2
    
    return new_array


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
print("The rotated array by 3 to the right is:", rotate_element(nums, k))
'''
