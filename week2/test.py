'''edge cases:
    duplicate
    can it be negative
    size of input
    time/ space complexity
    can I creating  another data structure
    wihtout using more space
    am I doing this every set in the data set
    

    '''

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

option:2

s = set()
s.add(arr[0])
for i in range(1, len(arr)):
    complement = x - arr[i]
    if complement in s:
        return(complement, [a[i]])
    s.add[a[i]]
return(None)

time:
space: linertime( will contain all the elements in array if the set doesnt exist)
    
