# Description
# You are given a strings, you have to find the count of all such substrings which start and ends with the same character.


# Given input:
s = "abcab"
n = len(s)

# output = 7


# approach
# 1. find substring 
# 2. check 

count = 0
for i in range(n):
    for j in range(i, n):
        if s[i] == s[j]:
            count+=1
        
print(count)


