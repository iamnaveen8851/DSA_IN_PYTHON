# Substrings starting with K
# Description
# You are given a string A, of length N, and a character K. Find all the substrings of A, that start with K. Refer the sample I/O for better understanding.
# # Note: The string contains lower case letters only.


# Given input

s = "aman"
n = len(s)
k = "a"

# output 
# 6


# approach:

# run two nested loops 
# create subStrings
# check if substring of 0th index  === k true then count

count = 0
for i in range(n):
    for j in range(i, n):
        subStr = s[i:j+1]
        if subStr[0] == k:
            count+=1
print(count)