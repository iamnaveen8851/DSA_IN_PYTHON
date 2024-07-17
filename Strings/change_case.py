# Change the case

# Description

# Given a string containing both Uppercase and Lowercase characters

# • You need to change the Uppercase into Lowercase and Lowercase into Uppercase.

# You need to make a function to change the case

# Create a function with the name changeCase Which takes one alphabet either in uppercase or lowercase and returns an opposite case of that.
# Suppose you passed A in the changeCase function so it will return a and if you passed a it will return A

# Note: Make sure to make a function to complete the code.

# Given input 

s = "aBbcd"
n = len(s)

# output 
# AbBCD


# to convert the cases with this function 
def changeCase(char):
    if char.isupper():
        return char.lower()
    elif char.islower():
        return char.upper()


def solve(s):
    bag = ""
    for i in range(n):
        cases = changeCase(s[i])
        bag+= cases
    return bag
print(solve(s))


    


