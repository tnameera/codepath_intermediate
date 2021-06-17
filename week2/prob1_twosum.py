"""
Problem 1 - Find a pair with given sum
Given an array of size n and a number x, determine the first two elements in the array, if any, whose sum is exactly x.
"""

def pairSum(nums, target):
    """
    time complex:O(N) for i in range(len(nums)):
    nums[i] in pairmaps: is O(1)
    Space complexity: O(N) for pairmaps
    """
    maps={}
    for i in nums:
        item = nums[i]
        #print(i, pairmaps)
        complement = target - item
        #print (complement)
        if item in maps:
            return True
        else:
            maps[complement] = item# the key value of pairmaps(complement) = nums[i]
    return False

print(pairSum([2,7,9,4],9))
print(pairSum([2,6,9,4],9))


def pairSum_elems(nums, target):
    """
    time complex:O(N) for i in range(len(nums)):
    nums[i] in pairmaps: is O(1)
    Space complexity: O(N) for pairmaps
    """
    maps={}
    #maps[keys:value]
    for item in range(len(nums)):
        nums[item] = item
        #print(i, pairmaps)
        complement = target - item
        #print (complement)
        if item in maps:
            return [maps[item],item]# gives the value of the key and nums[i] the value of the indecies
        else:
            maps[complement] = item# 
    return (None)

print(pairSum_elems([2,7,9,4],9))
print(pairSum_elems([2,6,9,4],9))

print('-----------')
def twoSum_indices(nums, target):
    """
    time complex:O(N) for i in range(len(nums)):
    nums[i] in pairmaps: is O(1)
    Space complexity: O(N) for pairmaps
    """
    maps={}
    for item in range(len(nums)):
        nums[item] = item
        #print(i, pairmaps)
        complement = target - item
        #print (complement)
        if item in maps:
            return [maps[item],item]
            
        else:
            maps[complement] = item #{7:0}
        return (None)

print(twoSum_indices([2,5,7,9,4],9))
print(twoSum_indices([2,6,9,4],9))



def twoSum(nums,x):
  pairSum = {}
  for i in range(len(nums)):
    complement = x - nums[i]
    if nums[i] in pairSum:
      return(pairSum[nums[i]],nums[i])
    else:
      pairSum[complement] = nums[i]

    return(None)

nums = [3, 2, 6, 9, 5]
x = 9
nums = []
x = 9
print(twoSum(nums,x))
"""
since we need to find a pair let
a + b = target
suppose a = 7 and b = 2 and target is 2+7 =9
ways of finding 9 is 
2+7
9+0
5+4......
so try to find the first element in map so that we can look for the second
a = target - nums[i] here nums[i] = nums[0] = 2
so if our target is 9 and first elemenet is the pair is 2 
then we can start looking for the second which will be (9-2 = 7)
and we can call this compliment in this function
we itterate thrugh the array looking for this pair
brute force: takes make time goin througn double loop:n(n2)
to avoid this we use the hashmap: o(n)
once we find it we return the pair
else we return none


for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[j] == target - nums[i]:
            return(nums[i], nums[j])
        

        
"""

