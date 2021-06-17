"""
Problem 2 - Kth frequent number
Find the element that appears k number of times in an array.

Input: [8, 7, 9, 6, 7, 5, 1], k = 2
Output: 7

"""

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            sum = nums[i]+nums[j]
            if sum == target:
                return True
    return False

print(twoSum([4,7,9,2],9))

