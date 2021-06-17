"""
Problem 2 - Kth frequent number
Find the element that appears k number of times in an array.

Input: [8, 7, 9, 6, 7, 5, 1], k = 2
Output: 7

"""
def kfrequency(nums, k):
    #task 1: count the frquencies
    counter = {}
    for item in range(len(nums)):
        #print(i,nums[i],counter)
        nums[item] = item
        if item in counter:
            counter[item] += 1 
        else:
            counter[item]= 1   
    #print(counter)

    #task 2: which elements has frequency = k
    for key in counter:
        #print(key, counter[key])
        if counter[key] == k:
            return (key)
    return(-1)
nums = [8, 7, 9, 6, 7, 5, 1]
#nums = [8, 7, 9, 6, 5, 1]
k = 2
print(kfrequency(nums, k))

"""
time complexities:for i in range(len(nums)):O(N)
if nums[i] in counter: because of dict the tiem complexiity is O(1)
for key in counter: Let K be unique nb of elements of nums then this is O(K)
but as K <= N the whoel algorithm is O(N)+ O(K) = O(N)


I am not sure how much space the dictionary takes 
space complexity worse case when all characters are unique space complexity is O(N)


edge cases:
can 
k = 0?
nums = empty?
task 1: count the frequencies
#frequency of the numbers
#how many times each elements show up in the list
task 2: which elements has frequency = k
"""



"""
option 2 from class

"""



