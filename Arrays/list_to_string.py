# List to String


# Description

# You are given a list A of n elements. Write a program that processes the elements of the list and generates a string from the elements present in the list.
# For instance: If elements of the list are 3 50 9.8 => the output string should be "35098" (without quotes). But in case of elements are negative (lesser than 0), your string should con
# tain 0 instead of that number.
# Suppose elements of the list are 2-4 6 8-9, the string generated should be 20680 because -4 and -9 are negative elements, so your string contains 0 instead of that number.


# Given input 
arr = [2, -4, 6, 8, -9]
n = len(arr)

# output  
# 20680

def list_to_string(arr, n):
    bag = ""
    for i in range(n):
        if arr[i] < 0:
            bag+= str(0)
        else:
            bag+= str(arr[i])
    return bag
print(list_to_string(arr, n))