"""
input = [3,4,3,5]
{3:2,4:1,5:1}#hashset
 -> {4,5}
output = 9
"""
def uniqeSet(nums):
    counterMap = {}
    #uniqueSum = {element, count}
    #try to indent the elements in the hashset
    for item in nums:
        if item in counterMap:
            counterMap[item] += 1
        else:
            counterMap[item] = 1

    # so you are exoecting a hash set
    #uniqeSum = {3:2,4:1,5:1}
    # call total = 0  for counting the sum of unique values
    # To determine the unique elments we need loop through the set to check 
    # once you find a unique element increment total
    
    total = 0
    for item in counterMap.keys():
        if counterMap[item] == 1:
            total = total + item
        
    return total


#uniqset 2
def uniqeSet2(nums):
    counterMap = {}
    #uniqueSum = {element, count}
    #try to indent the elements in the hashse

    for i in range(len(nums)):
        item = nums[i]
        if item in counterMap:
            counterMap[item] += 1
        else:
            counterMap[item] = 1

    # so you are exoecting a hash set
    #uniqeSum = {3:2,4:1,5:1}
    # call total = 0  for counting the sum of unique values
    # To determine the unique elments we need loop through the set to check 
    # once you find a unique element increment total
    
    total = 0
    for item in counterMap.keys():
        if counterMap[item] == 1:
            total = total +item
        
    return total

#test1
nums = [3,4,3,5]
print(uniqeSet2(nums))

#test1
nums = []
print(uniqeSet2(nums))

#test1
nums = [1,1,1]
print(uniqeSet2(nums))


    


