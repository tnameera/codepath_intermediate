#recurssion f(n) = f(n-1)+ f(n-2)

#input =n
#output =[]

def fib1(n):
    #base case:
    if n == 0:
        return 1
    if n == 1:
        return 2  

    return (fib1(n-1)+ fib1(n-2))


def fibLessThanN(n):
    nums = [1,2]
    while nums[-1] < n:
        nums.append(nums[-1]+nums[-2])
    print(nums, len(nums))
    sum = 0
    for i in range(len(nums)-1):
        if nums[i] % 2 == 0:
            sum = sum + nums[i]

    return sum

print(fibLessThanN(4000000))

