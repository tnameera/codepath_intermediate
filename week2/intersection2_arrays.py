'''
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must be unique and you may return the result in any order.

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
'''



#res = set() #set never carry duplicate
#res2 = []#list which can carry a duplicate

#edge
#what is num2 is bigger? if len(num1) < len(num2): num1, num2 = num2, num1
#what if one of them is empty
#what if their is no unique numbers here
#is the function always to return an output
'''
for num in nums1:
    if num in nums2:
        res.add(num)
        res2.append(num)
        '''

def setIntersection(nums1, nums2):

    nums1 = set(nums1) #o(n)
    nums2 = set(nums2) #o(m)
    res = set()

    for num in nums1: #o(n) where n is the lenght of num1
        if num in nums2: #o(1) for sets, o(m) for lists m is the length if num2
            res.add(num)#o(1)
            #res2.append(num)#o(1)
    return (res)


nums1 = [1,2,2,1]
nums2 = [2,2]
print(setIntersection(nums1, nums2))   
#print(res2) 

for i, num in enumerate(nums1):
    print(i, num)