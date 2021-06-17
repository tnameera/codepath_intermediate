"""
Problem 1 - Find a pair with given sum
Given an array of size n and a number x, determine the first two elements in the array, if any, whose sum is exactly x.
"""

def twoSum(nums, target):
    """
    time complex:O(N) for i in range(len(nums)):
    nums[i] in pairmaps: is O(1)
    Space complexity: O(N) for pairmaps
    """
    pairmaps={}
    for i in range(len(nums)):
        #print(i, pairmaps)
        complement = target - nums[i]
        print (complement)
        if nums[i] in pairmaps:
            return True
        else:
            pairmaps[complement] = nums[i]
    return False

print(twoSum([2,7,9,4],9))
print(twoSum([2,6,9,4],9))


def twoSum_elems(nums, target):
    """
    time complex:O(N) for i in range(len(nums)):
    nums[i] in pairmaps: is O(1)
    Space complexity: O(N) for pairmaps
    """
    pairmaps={}
    for i in range(len(nums)):
        #print(i, pairmaps)
        complement = target - nums[i]
        print (complement)
        if nums[i] in pairmaps:
            return [pairmaps[nums[i]],nums[i]]
        else:
            pairmaps[complement] = nums[i]
    return False

print(twoSum_elems([2,7,9,4],9))
print(twoSum_elems([2,6,9,4],9))

def twoSum_indices(nums, target):
    """
    time complex:O(N) for i in range(len(nums)):
    nums[i] in pairmaps: is O(1)
    Space complexity: O(N) for pairmaps
    """
    pairmaps={}
    for i in range(len(nums)):
        #print(i, pairmaps)
        complement = target - nums[i]
        print (complement)
        if nums[i] in pairmaps:
            return [pairmaps[nums[i]],i]
        else:
            pairmaps[complement] = i
    return False

print(twoSum_indices([2,7,9,4],9))
print(twoSum_indices([2,6,9,4],9))