
"""
Given a number, return the next smallest prime number

Examples:
Input: 3
Output: 5
"""
def isPrime(n):
     
    # Corner cases
    if(n <= 1):
        return False
     
    for i in range(2,n,1):
        if(n % i == 0):
            return False
     
    return True


    # Function to return the smallest
    # prime number greater than N
def nextPrime(N):
 
    # Base case
    if (N <= 1):
        return 2
        #2 is the smallest prime number
 
    prime = N
    found = False
 
    # Loop continuously until isPrime returns
    # True for a number greater than n
    while(not found):
        prime = prime + 1
 
        if(isPrime(prime) == True):
            found = True
 
    return prime
 
# Driver code
N = 3
print(nextPrime(N))


def isPrime(n):
    if(n<=1):
        #checkign if the given n is postive interger. since prime is positive integer
        return False
    
    # 2 is the smallest prime so starting with 2
    for i in range(2,n,1):
        #prime is only divisible by itself and 1
        if(n % i == 0):
            return False
        
    return True


def nextPrime(N):

    if (N<=1):
        return 2

    prime = N
    found = False

    while(not found):
        # prime is greater than n
        prime = prime +1


        if(isPrime(prime) == True):
            found = True
        
    return (prime)

N = 3
print(nextPrime(N))



    
    






