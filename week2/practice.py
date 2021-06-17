"""
Problem 2 - Kth frequent number
Find the element that appears k number of times in an array.

Input: [8, 7, 9, 6, 7, 5, 1], k = 2
Output: 7

"""

def kfrequency(nums,k):
    #count the frequencies
    counter = {}
    # counter{keys:values}
    for i in range(len(nums)):
        items = nums[i]
        if items in counter:
            counter[items] += 1
        else:
            counter[items] = 1


    # which element has a fequency = k

    for key in counter.key():    
        if counter[key] == k:# basically tryting to see if the values are same 
            return True

    return False

#test-case 1
nums = []
k = 0
print(kfrequency(nums,k))

#test-case 2
nums = []
k = 0
print(kfrequency(nums,k))

#test-case 
nums = [1,1,1]
k = 0
print(kfrequency(nums,k))



