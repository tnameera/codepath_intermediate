"""
big -o notation:


time complexity: 

array of length (n)
1.f(a)-> 1+a[0]
returns sum of the interger 1 and the first elmenet of the array


2.f(a)-> sum(a)
iterates through every elements in array and sums them up


method 1:
# Python 3 code to find sum 
# of elements in given array 
def _sum(arr): 
      
    # initialize a variable
    # to store the sum
    # while iterating through
    # the array later
    sum=0
      
    # iterate through the array
    # and add each element to the sum variable
    # one at a time
    for i in arr:
        sum = sum + i
          
    return(sum) 
  
# driver function 
arr=[] 
# input values to list 
arr = [12, 3, 4, 15] 
  
# calculating length of array 
n = len(arr) 
  
ans = _sum(arr) 
  
# display sum 
print ('Sum of the array is ', ans) 
  
# This code is contributed by Himanshu Ranjan 
Output:
method:2

# Python 3 code to find sum 
# of elements in given array
# driver function
arr = []
  
# input values to list
arr = [12, 3, 4, 15]
  
# sum() is an inbuilt function in python that adds 
# all the elements in list,set and tuples and returns
# the value 
ans = sum(arr)
  
# display sum
print ('Sum of the array is ',ans)
  
# This code is contributed by Dhananjay Patil


3.f(a)-> pair(a)[1,2,3]
generates a bunch of pair of numbers 
output: [1,1],[1,2],[1,3],[2,1].....
2 nested for loop


# Python3 implementation to find all
# Pairs possible from the given Array
 
# Function to prall possible
# pairs from the array
def printPairs(arr, n):
 
    # Nested loop for all possible pairs
    for i in range(n):
        for j in range(n):
            print("(",arr[i],",",arr[j],")",end=", ")
 
# Driver code
 
arr=[1, 2]
n = len(arr)
 
printPairs(arr, n)
 
# This code is contributed by mohit kumar 29

space complexity: o(n)+o(n) = n^2 2 nested loops


"""


