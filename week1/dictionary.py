classes = dict()

classes['nameera'] = ['cs', 'math', 'architecture']

classes['hafiz'] = ['cs', 'math', 'economics']

print(classes)

print(classes['hafiz'])

print(classes['hafiz'][1])

age = {}

age['nameera'] = 50
age['hafiz'] = 'forever21'
print(age)

for key in age:
    print('key:',key)
    print('value:', age[key])
    print('-'*10)


def twoSum(nums, target):
    pairmaps={}
    for i in range(len(nums)):
        print(i, pairmaps)
        complement = target - nums[i]
        if nums[i] in pairmaps:
            return True
        else:
            pairmaps[complement] = i
    return False

print(twoSum([2,7,9,4],9))
print(twoSum([2,6,9,4],9))