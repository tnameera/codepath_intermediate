#input 2
#output 1

#fib[0] = 0
#fib[1] = 1
#fib[2] = 1
#recurssion fib(n) = fib(n-1)+ fib(n-2)
#base case:
#def fibonacci(n):
    #if n == 0:
        #return 0
    #if n == 1:
        #return 1 
    #return(fibonacci(n-1)+ fibonacci(n-2))

def fibonacci(n):
    nums = [0,1]
    for i in range(2,n+1,1):
        nums.append(nums[-1]+ nums[-2])
    return(nums[-1])
print(fibonacci(10))


    



#print(fibonacci(2))
#print(fibonacci(7))
#print(fibonacci(10))

