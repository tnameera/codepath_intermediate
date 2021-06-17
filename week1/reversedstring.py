"""
Write a function that reverses a string.

Example:
Input: "hello"
Output: "olleh"
"""

def reverse(s):
    result = ""
    for i in range(len(s)-1,-1,-1):
        result = result +s[i]
    return(result)

print(reverse("hafiz"))

