"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""

def longeststring(s):
    map = {}
    map_start = 0
    map_len = 0
    map_longest = 0

    for i, letter in enumerate(s):
        # example s =[ 1,2,3]
        #(0,1)(1,2)(2,3)
        #for i in range(len(s)):
        # letter = s[i]

        if letter in map and map[letter] >= map_start:
            map_start = map[letter] + 1
            #example:"abcabcbb" if conditions are met
            #map letter for first match is 3 for 'a'
            #so now map[letter]+1 = 3+1 = 4 ie 'b'
            #the second loop will start from 'b' and move forward
            map_len = i - map[letter]
            #"abcabcbb"
            #"01234567"
            #example:i = 3 and map[letter] = 0
            #3 - 0 = 3
            map[letter] = i
            #example map[letter] = 3 now 

        else:
            map[letter] = i
            map_len += 1
            if map_len > map_longest:
                 map_longest = map_len



    return(map_longest)

s =[ 1,2,3]
print( longeststring(s))
            
