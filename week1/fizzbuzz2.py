
def fizzbuzz(nums):
    for each in nums:
        if (each % 3 == 0 and each % 5 == 0):
            print("fizzbuzz")
        elif (each % 3 == 0):
            print("fizz")
        elif (each % 5 == 0):
            print("buzz")
        else:
            print(each)
nums = [3,5,15,2,10]
fizzbuzz(nums)



