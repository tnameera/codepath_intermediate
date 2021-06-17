"""
Write a function that takes in two strings and returns true if the second string is substring of the first, and false otherwise.

Examples: 
Input: laboratory, rat
Output: true

Input: cat, meow
Output: false

"""

s2 = "rratt"
s1 = "rat"

M = len(s1)
N = len(s2)

for i in range(0,N-M+1,1):
    print(i,"----")
    for j in range(0,M,1):
        print(j,i+j,s2[i+j],s1[j])
        if (s2[i+j] != s1[j]):
            print('break')
            break
    if j == M-1:
        print(True)

print(False)
