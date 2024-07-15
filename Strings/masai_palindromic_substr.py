# Masai Palindromic Substring

# Description

# You are provided a string s.

# Write a program that returns length of the longest palindromic substring of that string.


# Given Input 
s = "thisracecarisgood"
n = len(s)


# approach 
# 1. create substring 
# 2. check if a substring is  a palindrome or not 
# 3. if its a palindromic substring store its length in a variable 
# 4. take a variable maxLength = 0
# 5. find maximum value by comparing the length palindromic substring with maxLength and store the max value inside the maxLength 

def isPalindrome(s):
    return s == s[::-1]

def findSubStr(s, n):
    maxLength = 0
    for i in range(n):
        for j in range(n):
            subStr = s[i:j+1]
            if (isPalindrome(subStr)):
                currLength = len(subStr)
                maxLength = max(currLength, maxLength)
    print(maxLength)

findSubStr(s, n)

