"""
Problem 3 (Challenge) - Longest Consecutive Subsequence
Given an unsorted array of integers, we want to find the length of the longest subsequence such that elements in the subsequence are consecutive integers. The consecutive numbers can be in any order.

For example:

Input: [1, 9, 3, 10, 4, 20 , 2]
Output: 4
[1, 3, 4, 2] is the longest subsequence of consecutive elements.

base case for empty array
"""

def longestCons(nums):
    if not nums:
        return 0

    nums.sort() # O(NlogN)
    #[1,2,3,4,9,10,20,21,22,23,24,25]

    long_streak = 1
    curr_streak = 1

    for i in range(1,len(nums)):#O(N)
        if nums[i] != nums[i-1]:# checking they are not equal
            if nums[i] == nums[i-1]+1: # checking is the sorted list is in incrementing order
                curr_streak += 1
            else:
                #update long_streak
                if curr_streak > long_streak:
                    long_streak = curr_streak
                curr_streak = 1 # reset curr_streak
    # if longest streak is at very end
    if curr_streak > long_streak:
        long_streak = curr_streak 
    return long_streak

"-------------------------------"
 
def longestCons(nums): 
    if not nums:
        return 0

    nums.sort() # merge sort
    #[1,2,3,4,9,10,20,21,22,23,24,25]

    long_streak = 1 #count
    curr_streak = 1 #longest count

    for i in range(len(nums)): # time complexities O(N)
        if nums[i] != nums[i-1]:
            if nums[i] == nums[i-1]+1:
                curr_streak += 1

            else:
                long_streak = max(long_streak,curr_streak)#0(1)
                curr_streak = 1

    return max(long_streak,curr_streak)







