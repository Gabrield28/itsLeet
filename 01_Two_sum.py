nums1 = [3,2,4]
target1 = 6

nums2 = [1, 3, 6, 9, 14, 20, 19]
target2 = 29

def twoSum(nums, target):

    valeurs = dict()
    
    for i, elements in enumerate(nums):
        
        complement = target - elements
        
        if complement in valeurs:
            
            return [valeurs[complement], i] 
        
        valeurs[elements] = i
        
    return []
        
    
liste1 = twoSum(nums1, target1)
print(liste1)

liste2 = twoSum(nums2, target2)
print(liste2)