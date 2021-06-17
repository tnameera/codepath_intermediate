""" hashmap to count the frequency of the elements in the list/array
    map ={4:1,1:2,2:2}
    then loop throught the map to fidn the element with single frequency
    here its 4 
    return 4
"""
nums = [4,1,2,1,2]

def singleNumber(nums):
    maps = {}
    for item in nums:
        if item in maps:
            maps[item] += 1
        else:
            maps[item] = 1
    #print(maps)


    for item in maps.keys():
        if maps[item] == 1:
            return(item)

print(singleNumber(nums))